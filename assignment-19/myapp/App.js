import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';

import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
} from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(true);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count >-10) {
      setCount(count - 1);
    }
  };

  const handleReset = () => {
    setCount(0);
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  const backgroundColor = isDarkMode ? '#0F172A' : '#F8FAFC';
  const cardColor = isDarkMode ? '#1E293B' : '#FFFFFF';
  const textColor = isDarkMode ? '#E2E8F0' : '#0F172A';

  return (
    <View style={[styles.container, { backgroundColor }]}>
      <View style={[styles.card, { backgroundColor: cardColor }]}>
        
        <Text style={styles.title}>
          Welcome piyush
          
          
        </Text>

        <Text style={[styles.subtitle, { color: textColor }]}>
          Building awesome apps with React Native 🚀
        </Text>

        <Text style={[styles.counterText, { color: textColor }]}>
          {count}
        </Text>

        <View style={styles.buttonRow}>
          <TouchableOpacity
            style={styles.button}
            onPress={handleDecrement}
          >
            <Text style={styles.buttonText}>-</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.button}
            onPress={handleIncrement}
          >
            <Text style={styles.buttonText}>+</Text>
          </TouchableOpacity>
        </View>

        <TouchableOpacity
          style={styles.resetButton}
          onPress={handleReset}
        >
          <Text style={styles.buttonText}>Reset</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.themeButton}
          onPress={toggleTheme}
        >
          <Text style={styles.buttonText}>
            Toggle Theme
          </Text>
        </TouchableOpacity>

        <Text style={styles.footer}>
          Future AI & Cyber Security Engineer 💻
        </Text>
      </View>

      <StatusBar style={isDarkMode ? 'light' : 'dark'} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  card: {
    width: '100%',
    borderRadius: 25,
    padding: 30,
    alignItems: 'center',

    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 8,
    },
    shadowOpacity: 0.3,
    shadowRadius: 10,

    elevation: 10,
  },

  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#38BDF8',
    marginBottom: 15,
    textAlign: 'center',
  },

  subtitle: {
    fontSize: 18,
    textAlign: 'center',
    lineHeight: 28,
    marginBottom: 25,
  },

  counterText: {
    fontSize: 55,
    fontWeight: 'bold',
    marginBottom: 25,
  },

  buttonRow: {
    flexDirection: 'row',
    marginBottom: 20,
  },

  button: {
    backgroundColor: '#2563EB',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 12,
    marginHorizontal: 10,
  },

  resetButton: {
    backgroundColor: '#DC2626',
    paddingVertical: 14,
    paddingHorizontal: 35,
    borderRadius: 12,
    marginBottom: 15,
  },

  themeButton: {
    backgroundColor: '#059669',
    paddingVertical: 14,
    paddingHorizontal: 35,
    borderRadius: 12,
    marginBottom: 25,
  },

  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },

  footer: {
    fontSize: 16,
    color: '#94A3B8',
    fontStyle: 'italic',
    textAlign: 'center',
  },
});