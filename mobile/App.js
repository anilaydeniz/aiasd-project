// mobile/App.js
// KitchenOps main mobile container with authentication flow & multi-screen navigation

import React, { useState, Component } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, SafeAreaView } from 'react-native';
import LoginScreen from './LoginScreen';
import PrepScreen from './PrepScreen';
import OrderScreen from './OrderScreen';
import ChatScreen from './ChatScreen';

class ErrorBoundary extends Component {
  state = { hasError: false, error: null };
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  componentDidCatch(error, info) {
    console.warn('KitchenOps UI error caught:', error, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <SafeAreaView style={{ flex: 1, backgroundColor: '#0f172a', justifyContent: 'center', alignItems: 'center', padding: 24 }}>
          <Text style={{ color: '#ef4444', fontSize: 20, fontWeight: 'bold', marginBottom: 12 }}>Application Encountered an Error</Text>
          <Text style={{ color: '#94a3b8', fontSize: 14, textAlign: 'center', marginBottom: 20 }}>
            {String(this.state.error?.message || 'Unexpected display error')}
          </Text>
          <TouchableOpacity
            onPress={() => this.setState({ hasError: false })}
            style={{ backgroundColor: '#0284c7', paddingHorizontal: 20, paddingVertical: 12, borderRadius: 8 }}
          >
            <Text style={{ color: '#ffffff', fontWeight: 'bold' }}>Restart Session</Text>
          </TouchableOpacity>
        </SafeAreaView>
      );
    }
    return this.props.children;
  }
}

export default function App() {
  const [session, setSession] = useState(null);
  const [activeTab, setActiveTab] = useState('prep');

  const safeUser = session
    ? (typeof session.user === 'object' && session.user !== null
        ? (session.user.email || session.user.user || 'chef@kitchenops.internal')
        : String(session.user || 'chef@kitchenops.internal'))
    : 'chef@kitchenops.internal';

  return (
    <ErrorBoundary>
      <View style={styles.container}>
        {!session ? (
          <LoginScreen
            onLoginSuccess={(user, token) => {
              const emailStr = typeof user === 'object' && user !== null
                ? (user.email || user.user || 'chef@kitchenops.internal')
                : String(user || 'chef@kitchenops.internal');
              setSession({ user: emailStr, token });
            }}
          />
        ) : (
          <View style={styles.appShell}>
            <View style={styles.content}>
              {activeTab === 'prep' ? (
                <PrepScreen
                  user={safeUser}
                  onLogout={() => setSession(null)}
                />
              ) : activeTab === 'orders' ? (
                <OrderScreen
                  user={safeUser}
                />
              ) : (
                <ChatScreen
                  user={safeUser}
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
                Orders
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.navItem, activeTab === 'chat' && styles.navItemActive]}
              onPress={() => setActiveTab('chat')}
            >
              <Text style={styles.navIcon}>🤖</Text>
              <Text style={[styles.navLabel, activeTab === 'chat' && styles.navLabelActive]}>
                AI Chat
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
    </ErrorBoundary>
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
