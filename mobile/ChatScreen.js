// mobile/ChatScreen.js
// serves: REQ-009, REQ-006
// KitchenOps AI Assistant mobile chatbot screen — initial UI scaffold

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
} from 'react-native';

export default function ChatScreen({ user }) {
  const [messages, setMessages] = useState([
    {
      id: '1',
      sender: 'system',
      text: 'Welcome to KitchenOps Assistant. You can ask about ingredient levels, recipes, and supplier restocks.',
    },
  ]);
  const [inputMessage, setInputMessage] = useState('');

  const handleSendDraft = () => {
    if (!inputMessage.trim()) return;
    const userMsg = {
      id: Date.now().toString(),
      sender: 'user',
      text: inputMessage.trim(),
    };
    setMessages((prev) => [...prev, userMsg]);
    setInputMessage('');
    // Draft stage: local UI scaffolding before wiring live backend POST /chat
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
    >
      <View style={styles.header}>
        <Text style={styles.headerTitle}>KitchenOps AI Assistant</Text>
        <Text style={styles.headerSubtitle}>Logged in as: {user || 'Chef'}</Text>
      </View>

      <ScrollView style={styles.messagesContainer} contentContainerStyle={styles.messagesContent}>
        {messages.map((msg) => (
          <View
            key={msg.id}
            style={[
              styles.messageBubble,
              msg.sender === 'user' ? styles.userBubble : styles.assistantBubble,
            ]}
          >
            <Text style={styles.senderLabel}>
              {msg.sender === 'user' ? 'Chef' : 'Kitchen Assistant'}
            </Text>
            <Text style={styles.messageText}>{msg.text}</Text>
          </View>
        ))}
      </ScrollView>

      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Ask assistant about inventory or recipes..."
          placeholderTextColor="#888"
          value={inputMessage}
          onChangeText={setInputMessage}
        />
        <TouchableOpacity style={styles.sendButton} onPress={handleSendDraft}>
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
    paddingBottom: 16,
    paddingHorizontal: 20,
    backgroundColor: '#1E293B',
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#F8FAFC',
  },
  headerSubtitle: {
    fontSize: 13,
    color: '#94A3B8',
    marginTop: 4,
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
    backgroundColor: '#3B82F6',
  },
  assistantBubble: {
    alignSelf: 'flex-start',
    backgroundColor: '#1E293B',
    borderWidth: 1,
    borderColor: '#334155',
  },
  senderLabel: {
    fontSize: 11,
    fontWeight: '600',
    color: '#94A3B8',
    marginBottom: 4,
  },
  messageText: {
    fontSize: 15,
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
    backgroundColor: '#3B82F6',
    paddingHorizontal: 16,
    height: 44,
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontWeight: 'bold',
    fontSize: 14,
  },
});
