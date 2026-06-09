# ============================================================
# E-COMMERCE ORDER PROCESSING SYSTEM — SOLID PRINCIPLES
# ============================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
import datetime

# ─────────────────────────────────────────────────────────────
# DATA MODEL
# ─────────────────────────────────────────────────────────────

@dataclass
class OrderItem:
    name: str
    price: float
    quantity: int

# ─────────────────────────────────────────────────────────────
# PRINCIPLE 3 — LSP + OCP
# Abstract base class: Order
# All concrete order types honour calculateTotal() contract
# ─────────────────────────────────────────────────────────────

class Order(ABC):
    def __init__(self, order_id: str, customer: str, items: List[OrderItem]):
        self.order_id  = order_id
        self.customer  = customer
        self.items     = items
        self.timestamp = datetime.datetime.now().isoformat()

    def base_total(self) -> float:
        return sum(i.price * i.quantity for i in self.items)

    @abstractmethod
    def calculate_total(self) -> float:
        """Every subclass MUST implement this — LSP guarantee."""
        ...

    def __repr__(self):
        return (f"Order[{self.order_id}] customer={self.customer} "
                f"total={self.calculate_total():.2f}")


class RegularOrder(Order):
    """Standard order — no modifications to total."""
    def calculate_total(self) -> float:
        return self.base_total()


class DiscountedOrder(Order):
    """OCP: add new order type without touching existing classes."""
    def __init__(self, *args, discount_pct: float = 10, **kwargs):
        super().__init__(*args, **kwargs)
        self.discount_pct = discount_pct

    def calculate_total(self) -> float:
        return self.base_total() * (1 - self.discount_pct / 100)


class PriorityOrder(Order):
    """Priority surcharge applied on top of base total."""
    SURCHARGE = 50.0

    def calculate_total(self) -> float:
        return self.base_total() + self.SURCHARGE


# ─────────────────────────────────────────────────────────────
# PRINCIPLE 4 — ISP
# Small, role-specific interfaces instead of one large interface
# ─────────────────────────────────────────────────────────────

class PaymentProcessor(ABC):
    """Interface for payment — only process()."""
    @abstractmethod
    def process(self, order: Order) -> bool:
        ...


class Notifier(ABC):
    """Interface for notification — only notify()."""
    @abstractmethod
    def notify(self, order: Order) -> None:
        ...


class OrderStorage(ABC):
    """Interface for persistence — only save()."""
    @abstractmethod
    def save(self, order: Order) -> None:
        ...


# ─────────────────────────────────────────────────────────────
# PRINCIPLE 2 — OCP
# New payment methods added WITHOUT modifying existing code
# ─────────────────────────────────────────────────────────────

class CreditCardProcessor(PaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"[CreditCard] Charged ₹{order.calculate_total():.2f} "
              f"for order {order.order_id}")
        return True


class UPIProcessor(PaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"[UPI] Payment of ₹{order.calculate_total():.2f} "
              f"initiated for order {order.order_id}")
        return True


class WalletProcessor(PaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"[Wallet] Debited ₹{order.calculate_total():.2f} "
              f"for order {order.order_id}")
        return True


# New method added later — zero changes to existing classes (OCP)
class NetBankingProcessor(PaymentProcessor):
    def process(self, order: Order) -> bool:
        print(f"[NetBanking] Transfer ₹{order.calculate_total():.2f} "
              f"for order {order.order_id}")
        return True


# ─────────────────────────────────────────────────────────────
# PRINCIPLE 2 — OCP: New notification channels
# ─────────────────────────────────────────────────────────────

class EmailNotifier(Notifier):
    def notify(self, order: Order) -> None:
        print(f"[Email] Order {order.order_id} confirmed for {order.customer}")


class SMSNotifier(Notifier):
    def notify(self, order: Order) -> None:
        print(f"[SMS] Order {order.order_id} placed. Total ₹{order.calculate_total():.2f}")


class PushNotifier(Notifier):
    def notify(self, order: Order) -> None:
        print(f"[Push] 🔔 Your order {order.order_id} is being processed!")


# ─────────────────────────────────────────────────────────────
# PRINCIPLE 2 — OCP: New storage mechanisms
# ─────────────────────────────────────────────────────────────

class DatabaseStorage(OrderStorage):
    def save(self, order: Order) -> None:
        print(f"[DB] Saved order {order.order_id} to database.")


class FileStorage(OrderStorage):
    def save(self, order: Order) -> None:
        filename = f"order_{order.order_id}.txt"
        with open(filename, "w") as f:
            f.write(str(order))
        print(f"[File] Order {order.order_id} written to {filename}")


# ─────────────────────────────────────────────────────────────
# PRINCIPLE 1 — SRP
# OrderService only orchestrates; payment/notify/storage are separate
#
# PRINCIPLE 5 — DIP
# Depends on abstractions (PaymentProcessor, Notifier, OrderStorage)
# Concrete implementations injected via constructor
# ─────────────────────────────────────────────────────────────

class OrderService:
    def __init__(
        self,
        payment_processor: PaymentProcessor,   # DIP: abstraction
        notifiers: List[Notifier],             # DIP: abstraction
        storage: OrderStorage                  # DIP: abstraction
    ):
        self._processor = payment_processor
        self._notifiers = notifiers
        self._storage   = storage

    def place_order(self, order: Order) -> None:
        print(f"\n{'='*50}")
        print(f"Processing: {order}")

        # Step 1 — Payment
        success = self._processor.process(order)
        if not success:
            print("[OrderService] Payment failed. Order aborted.")
            return

        # Step 2 — Notify
        for notifier in self._notifiers:
            notifier.notify(order)

        # Step 3 — Persist
        self._storage.save(order)
        print(f"[OrderService] Order {order.order_id} placed successfully.")
        print('='*50)


# ─────────────────────────────────────────────────────────────
# CLIENT CODE — Wiring via Dependency Injection
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    items = [
        OrderItem("Laptop", 75000, 1),
        OrderItem("Mouse",   1500, 2),
    ]

    # Use Case 1: Regular order, UPI, Email + SMS, DB storage
    order1 = RegularOrder("ORD001", "Amit Sharma", items)
    service1 = OrderService(
        payment_processor = UPIProcessor(),
        notifiers         = [EmailNotifier(), SMSNotifier()],
        storage           = DatabaseStorage()
    )
    service1.place_order(order1)

    # Use Case 2: Discounted order, Credit Card, all notifiers, File storage
    order2 = DiscountedOrder("ORD002", "Priya Singh", items, discount_pct=15)
    service2 = OrderService(
        payment_processor = CreditCardProcessor(),
        notifiers         = [EmailNotifier(), SMSNotifier(), PushNotifier()],
        storage           = FileStorage()
    )
    service2.place_order(order2)

    # Use Case 3: Priority order, Wallet, Push only, DB storage
    order3 = PriorityOrder("ORD003", "Rahul Verma", items)
    service3 = OrderService(
        payment_processor = WalletProcessor(),
        notifiers         = [PushNotifier()],
        storage           = DatabaseStorage()
    )
    service3.place_order(order3)