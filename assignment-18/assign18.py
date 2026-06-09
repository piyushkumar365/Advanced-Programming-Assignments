"""
score_processor.py

Program to read an integer score from a file,
multiply it by 10, and handle exceptions properly.

Run tests using:
pytest score_processor.py -v
"""

import pytest


# 1. CLASS DEFINITION

class ScoreProcessor:

    def process_score_file(self, file_path: str) -> int:
        """
        Reads an integer from a file,
        multiplies it by 10,
        and returns the result.
        """

        try:
            # Open file and read data
            with open(file_path, "r") as file:
                data = file.read().strip()

            # Convert string into integer
            score = int(data)

        # File not found exception
        except FileNotFoundError:
            print("Error: File not found.")
            raise

        # Invalid number format exception
        except ValueError:
            print("Error: Invalid data format in file.")
            raise

        # Executes only if no exception occurs
        else:
            print("Data processed successfully")
            return score * 10

        # Always executes
        finally:
            print("File cleanup completed")


# 2. PYTEST TEST CASES

def test_valid_score_file(tmp_path):
    """
    Test successful calculation using valid file input.
    """

    # Create temporary file
    file = tmp_path / "score.txt"
    file.write_text("8")

    processor = ScoreProcessor()

    # Expected result = 8 * 10 = 80
    result = processor.process_score_file(str(file))

    assert result == 80


def test_missing_file():
    """
    Test handling of missing file using pytest.raises.
    """

    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_file.txt")


def test_invalid_data_format(tmp_path):
    """
    Test handling of invalid data format.
    """

    # Create temporary file with invalid data
    file = tmp_path / "invalid.txt"
    file.write_text("abc")

    processor = ScoreProcessor()

    with pytest.raises(ValueError):
        processor.process_score_file(str(file))


# 3. MAIN FUNCTION

if __name__ == "__main__":

    print("Running Manual Demonstration\n")

    processor = ScoreProcessor()

    # Create sample file
    sample_file = "sample_score.txt"

    with open(sample_file, "w") as file:
        file.write("9")

    try:
        result = processor.process_score_file(sample_file)
        print("Final Result =", result)

    except Exception:
        print("Program terminated due to an error.")

    print("\nProgram Execution Completed")