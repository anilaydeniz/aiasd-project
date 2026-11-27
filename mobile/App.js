// mobile/App.js
// KitchenOps main mobile container with authentication flow & multi-screen navigation
// Integrates bottom navigation bar with transparent PNG icons and safe padding

import React, { useState, Component } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  SafeAreaView,
  Image,
  ImageBackground,
  Platform,
  StatusBar,
} from 'react-native';
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
        <SafeAreaView style={styles.errorContainer}>
          <Text style={styles.errorHeading}>Application Display Error</Text>
          <Text style={styles.errorMessage}>
            {String(this.state.error?.message || 'Unexpected display error')}
          </Text>
          <TouchableOpacity
            onPress={() => this.setState({ hasError: false })}
            style={styles.restartButton}
          >
            <Text style={styles.restartButtonText}>Restart KitchenOps</Text>
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
    ? typeof session.user === 'object' && session.user !== null
      ? session.user.email || session.user.user || 'chef@kitchenops.internal'
      : String(session.user || 'chef@kitchenops.internal')
    : 'chef@kitchenops.internal';

  const isPrepActive = activeTab === 'prep';
  const isOrdersActive = activeTab === 'orders';
  const isChatActive = activeTab === 'chat';

  return (
    <ErrorBoundary>
      <StatusBar barStyle="dark-content" backgroundColor="transparent" translucent={true} />
      <SafeAreaView style={styles.safeContainer}>
        {!session ? (
          <LoginScreen
            onLoginSuccess={(user, token) => {
              const emailStr =
                typeof user === 'object' && user !== null
                  ? user.email || user.user || 'chef@kitchenops.internal'
                  : String(user || 'chef@kitchenops.internal');
              setSession({ user: emailStr, token });
            }}
          />
        ) : (
          <ImageBackground
            source={require('./assets/arka_plan_ic_ekranlar.webp')}
            style={styles.mainShell}
            resizeMode="cover"
          >
            {/* Active Screen View */}
            <View style={styles.screenContainer}>
              {activeTab === 'prep' && (
                <PrepScreen
                  user={safeUser}
                  onNavigate={setActiveTab}
                  onLogout={() => setSession(null)}
                />
              )}
              {activeTab === 'orders' && (
                <OrderScreen
                  user={safeUser}
                  onNavigate={setActiveTab}
                  onLogout={() => setSession(null)}
                />
              )}
              {activeTab === 'chat' && (
                <ChatScreen
                  user={safeUser}
                  onNavigate={setActiveTab}
                  onLogout={() => setSession(null)}
                />
              )}
            </View>

            {/* Bottom Navigation Bar with Safe Padding */}
            <View style={styles.navBar}>
              {/* Tab 1: Prep */}
              <TouchableOpacity
                style={[styles.navItem, isPrepActive && styles.navItemActive]}
                onPress={() => setActiveTab('prep')}
              >
                <Image
                  source={require('./assets/icons/tab_prep.png')}
                  style={[
                    styles.navIcon,
                    isPrepActive ? styles.navIconActive : styles.navIconInactive,
                  ]}
                  resizeMode="contain"
                />
                <Text
                  style={[
                    styles.navLabel,
                    isPrepActive ? styles.navLabelActive : styles.navLabelInactive,
                  ]}
                >
                  Prep
                </Text>
              </TouchableOpacity>

              {/* Tab 2: Orders */}
              <TouchableOpacity
                style={[styles.navItem, isOrdersActive && styles.navItemActive]}
                onPress={() => setActiveTab('orders')}
              >
                <Image
                  source={require('./assets/icons/tab_orders.png')}
                  style={[
                    styles.navIcon,
                    isOrdersActive ? styles.navIconActive : styles.navIconInactive,
                  ]}
                  resizeMode="contain"
                />
                <Text
                  style={[
                    styles.navLabel,
                    isOrdersActive ? styles.navLabelActive : styles.navLabelInactive,
                  ]}
                >
                  Orders
                </Text>
              </TouchableOpacity>

              {/* Tab 3: AI Chat */}
              <TouchableOpacity
                style={[styles.navItem, isChatActive && styles.navItemActive]}
                onPress={() => setActiveTab('chat')}
              >
                <Image
                  source={require('./assets/icons/tab_ai_chat.png')}
                  style={[
                    styles.navIcon,
                    isChatActive ? styles.navIconActive : styles.navIconInactive,
                  ]}
                  resizeMode="contain"
                />
                <Text
                  style={[
                    styles.navLabel,
                    isChatActive ? styles.navLabelActive : styles.navLabelInactive,
                  ]}
                >
                  AI Chat
                </Text>
              </TouchableOpacity>
            </View>
          </ImageBackground>
        )}
      </SafeAreaView>
    </ErrorBoundary>
  );
}

const styles = StyleSheet.create({
  safeContainer: {
    flex: 1,
    backgroundColor: '#EDF2F7',
  },
  mainShell: {
    flex: 1,
    backgroundColor: '#EDF2F7',
  },
  topHeader: {
    backgroundColor: 'rgba(255, 255, 255, 0.94)',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingTop: Platform.OS === 'android' ? (StatusBar.currentHeight || 28) + 8 : 12,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#CBD5E1',
  },
  brandRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  headerLogo: {
    width: 32,
    height: 32,
    borderRadius: 8,
    marginRight: 10,
  },
  headerAppTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
  },
  headerStationSubtitle: {
    fontSize: 10.5,
    color: '#64748B',
  },
  logoutButton: {
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  logoutButtonText: {
    fontSize: 11,
    color: '#475569',
    fontWeight: '600',
  },
  screenContainer: {
    flex: 1,
    backgroundColor: 'transparent',
  },
  navBar: {
    flexDirection: 'row',
    backgroundColor: '#F8FAFC',
    borderTopWidth: 1,
    borderTopColor: '#CBD5E1',
    paddingTop: 8,
    paddingBottom: Platform.OS === 'ios' ? 28 : 38, // Elevated safe padding avoiding Android soft navigation keys
    elevation: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -3 },
    shadowOpacity: 0.08,
    shadowRadius: 8,
  },
  navItem: {
    flex: 1,
    alignItems: 'center',
    paddingVertical: 4,
  },
  navItemActive: {
    borderTopWidth: 0,
  },
  navIcon: {
    width: 24,
    height: 24,
    marginBottom: 3,
  },
  navIconActive: {
    tintColor: '#2F3B52',
  },
  navIconInactive: {
    tintColor: '#5E6E85',
  },
  navLabel: {
    fontSize: 11,
  },
  navLabelActive: {
    color: '#1E293B',
    fontWeight: '700',
  },
  navLabelInactive: {
    color: '#5E6E85',
    fontWeight: '500',
  },
  errorContainer: {
    flex: 1,
    backgroundColor: '#EDF2F7',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  errorHeading: {
    color: '#DC2626',
    fontSize: 18,
    fontWeight: '700',
    marginBottom: 8,
  },
  errorMessage: {
    color: '#64748B',
    fontSize: 13,
    textAlign: 'center',
    marginBottom: 20,
  },
  restartButton: {
    backgroundColor: '#1D4ED8',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 10,
  },
  restartButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
});
