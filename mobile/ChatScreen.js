// mobile/ChatScreen.js
// serves: REQ-009, REQ-006
// KitchenOps AI Assistant mobile chatbot screen — complete client with POST /chat and AI answer label

import React, { useState } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  KeyboardAvoidingView,
  Platform,
  ActivityIndicator,
} from 'react-native';
import { api } from './api';

export default function ChatScreen({ user }) {
  const [messages, setMessages] = useState([
    {
      id: 'init-1',
      sender: 'assistant',
      text: 'Hello Chef! I am your KitchenOps AI Assistant. Ask me about low stock buffers, recipe details, or replenishment purchase orders.',
      isAi: true,
    },
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [quotaRemaining, setQuotaRemaining] = useState(20);
  const [errorBanner, setErrorBanner] = useState('');

  const handleSendMessage = async () => {
    const trimmed = inputMessage.trim();
    if (!trimmed || loading) return;

    setErrorBanner('');
    const userMsg = {
      id: Date.now().toString(),
      sender: 'user',
      text: trimmed,
      isAi: false,
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputMessage('');
    setLoading(true);

    try {
      const res = await api('POST', '/chat', { message: trimmed });

      if (res.status === 200 && res.data) {
        const assistantMsg = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: res.data.reply || 'No response from assistant.',
          isAi: true,
        };
        setMessages((prev) => [...prev, assistantMsg]);
        if (typeof res.data.remaining_quota === 'number') {
          setQuotaRemaining(res.data.remaining_quota);
        }
      } else if (res.status === 429) {
        setErrorBanner(
          res.data?.detail || 'Daily chat limit reached (20 messages/day). Please try again tomorrow.'
        );
      } else if (res.status === 503) {
        setErrorBanner(
          res.data?.detail || 'AI Assistant service unavailable or timed out (HTTP 503). Please retry later.'
        );
      } else {
        setErrorBanner(res.data?.detail || `Server error (HTTP ${res.status}).`);
      }
    } catch (err) {
      setErrorBanner('Network error: unable to contact KitchenOps server.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
    >
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.headerRow}>
          <Text style={styles.headerTitle}>KitchenOps AI Assistant</Text>
          <View style={styles.quotaPill}>
            <Text style={styles.quotaText}>Daily: {quotaRemaining}/20</Text>
          </View>
        </View>
        <Text style={styles.headerSubtitle}>Logged in as: {user || 'chef@kitchenops.internal'}</Text>
      </View>

      {/* Error alert banner for 429 and 503 */}
      {errorBanner ? (
        <View style={styles.errorBanner}>
          <Text style={styles.errorText}>⚠ {errorBanner}</Text>
        </View>
      ) : null}

      {/* Message history */}
      <ScrollView
        style={styles.messagesContainer}
        contentContainerStyle={styles.messagesContent}
        keyboardShouldPersistTaps="handled"
      >
        {messages.map((msg) => (
          <View
            key={msg.id}
            style={[
              styles.messageBubble,
              msg.sender === 'user' ? styles.userBubble : styles.assistantBubble,
            ]}
          >
            {msg.isAi ? (
              <View style={styles.aiBadge}>
                <Text style={styles.aiBadgeText}>AI answer</Text>
              </View>
            ) : (
              <Text style={styles.senderLabel}>Chef</Text>
            )}
            <Text style={styles.messageText}>{msg.text}</Text>
          </View>
        ))}

        {loading ? (
          <View style={[styles.messageBubble, styles.assistantBubble, styles.loadingBubble]}>
            <View style={styles.aiBadge}>
              <Text style={styles.aiBadgeText}>AI answer</Text>
            </View>
            <ActivityIndicator size="small" color="#38BDF8" style={{ marginTop: 4 }} />
          </View>
        ) : null}
      </ScrollView>

      {/* Input container */}
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Ask AI assistant about inventory or recipes..."
          placeholderTextColor="#64748B"
          value={inputMessage}
          onChangeText={setInputMessage}
          editable={!loading}
          onSubmitEditing={handleSendMessage}
        />
        <TouchableOpacity
          style={[styles.sendButton, loading && styles.sendButtonDisabled]}
          onPress={handleSendMessage}
          disabled={loading}
        >
          <Text style={styles.sendButtonText}>Send</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  header: {
    paddingTop: 50,
    paddingBottom: 14,
    paddingHorizontal: 20,
    backgroundColor: '#1E293B',
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  headerRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 19,
    fontWeight: 'bold',
    color: '#F8FAFC',
  },
  headerSubtitle: {
    fontSize: 12,
    color: '#94A3B8',
    marginTop: 4,
  },
  quotaPill: {
    backgroundColor: '#0F172A',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#38BDF8',
  },
  quotaText: {
    fontSize: 11,
    color: '#38BDF8',
    fontWeight: '600',
  },
  errorBanner: {
    backgroundColor: '#7F1D1D',
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#EF4444',
  },
  errorText: {
    color: '#FEE2E2',
    fontSize: 13,
    fontWeight: '500',
  },
  messagesContainer: {
    flex: 1,
  },
  messagesContent: {
    padding: 16,
    gap: 12,
  },
  messageBubble: {
    maxWidth: '85%',
    borderRadius: 12,
    padding: 12,
  },
  userBubble: {
    alignSelf: 'flex-end',
    backgroundColor: '#2563EB',
  },
  assistantBubble: {
    alignSelf: 'flex-start',
    backgroundColor: '#1E293B',
    borderWidth: 1,
    borderColor: '#334155',
  },
  loadingBubble: {
    paddingVertical: 10,
    paddingHorizontal: 16,
  },
  aiBadge: {
    backgroundColor: '#0369A1',
    alignSelf: 'flex-start',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
    marginBottom: 6,
  },
  aiBadgeText: {
    color: '#F0F9FF',
    fontSize: 11,
    fontWeight: 'bold',
    letterSpacing: 0.3,
  },
  senderLabel: {
    fontSize: 11,
    fontWeight: '600',
    color: '#93C5FD',
    marginBottom: 4,
  },
  messageText: {
    fontSize: 14,
    color: '#F8FAFC',
    lineHeight: 20,
  },
  inputContainer: {
    flexDirection: 'row',
    padding: 12,
    backgroundColor: '#1E293B',
    borderTopWidth: 1,
    borderTopColor: '#334155',
    alignItems: 'center',
    gap: 8,
  },
  textInput: {
    flex: 1,
    height: 44,
    backgroundColor: '#0F172A',
    borderRadius: 8,
    paddingHorizontal: 12,
    color: '#F8FAFC',
    fontSize: 14,
    borderWidth: 1,
    borderColor: '#334155',
  },
  sendButton: {
    backgroundColor: '#2563EB',
    paddingHorizontal: 16,
    height: 44,
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sendButtonDisabled: {
    opacity: 0.5,
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontWeight: 'bold',
    fontSize: 14,
  },
});
