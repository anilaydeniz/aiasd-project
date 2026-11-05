// mobile/App.js
// KitchenOps main mobile container with authentication flow & multi-screen navigation

import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity } from 'react-native';
import LoginScreen from './LoginScreen';
import PrepScreen from './PrepScreen';
import OrderScreen from './OrderScreen';

export default function App() {
  const [session, setSession] = useState(null);
  const [activeTab, setActiveTab] = useState('prep');

  return (
    <View style={styles.container}>
      {!session ? (
        <LoginScreen
          onLoginSuccess={(user, token) => setSession({ user, token })}
        />
      ) : (
        <View style={styles.appShell}>
          <View style={styles.content}>
            {activeTab === 'prep' ? (
              <PrepScreen
                user={session.user}
                onLogout={() => setSession(null)}
              />
            ) : (
              <OrderScreen
                user={session.user}
              />
            )}
          </View>

          {/* Bottom Navigation Bar */}
          <View style={styles.navBar}>
            <TouchableOpacity
              style={[styles.navItem, activeTab === 'prep' && styles.navItemActive]}
              onPress={() => setActiveTab('prep')}
            >
              <Text style={styles.navIcon}>🍳</Text>
              <Text style={[styles.navLabel, activeTab === 'prep' && styles.navLabelActive]}>
                Kitchen Prep
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.navItem, activeTab === 'orders' && styles.navItemActive]}
              onPress={() => setActiveTab('orders')}
            >
              <Text style={styles.navIcon}>📦</Text>
              <Text style={[styles.navLabel, activeTab === 'orders' && styles.navLabelActive]}>
                Restock Orders
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.navItem}
              onPress={() => setSession(null)}
            >
              <Text style={styles.navIcon}>🚪</Text>
              <Text style={[styles.navLabel, styles.navLabelLogout]}>Log Out</Text>
            </TouchableOpacity>
          </View>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f172a',
  },
  appShell: {
    flex: 1,
  },
  content: {
    flex: 1,
  },
  navBar: {
    flexDirection: 'row',
    backgroundColor: '#1e293b',
    borderTopWidth: 1,
    borderTopColor: '#334155',
    paddingVertical: 10,
    paddingBottom: 24,
    justifyContent: 'space-around',
    alignItems: 'center',
  },
  navItem: {
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 4,
    borderRadius: 8,
  },
  navItemActive: {
    backgroundColor: '#0f172a',
    borderWidth: 1,
    borderColor: '#38bdf8',
  },
  navIcon: {
    fontSize: 18,
    marginBottom: 2,
  },
  navLabel: {
    color: '#94a3b8',
    fontSize: 12,
    fontWeight: '500',
  },
  navLabelActive: {
    color: '#38bdf8',
    fontWeight: 'bold',
  },
  navLabelLogout: {
    color: '#ef4444',
  },
});
