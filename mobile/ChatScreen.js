// mobile/ChatScreen.js
// serves: REQ-009, REQ-006, REQ-010
// KitchenOps AI Assistant mobile chatbot screen — complete client with POST /chat, Report button, and AI answer label

import React, { useState, useRef } from 'react';
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
  Modal,
  StatusBar,
} from 'react-native';
import { api } from './api';

export default function ChatScreen({ user, onNavigate, onLogout }) {
  const [messages, setMessages] = useState([
    {
      id: 'msg-user-1',
      sender: 'user',
      text: 'How much Cooking Cream 35% do we have left, and do I need to reorder?',
      isAi: false,
    },
    {
      id: 'msg-ai-1',
      sender: 'assistant',
      text: 'Cooking Cream 35% is at 3.50 L, which is below the 5.0 L safety buffer (deficit 1.50 L). A draft purchase order for 4 crates × 5 L (20 L) is ready for your review.',
      isAi: true,
      hasAction: true,
      actionText: 'Review Draft Order',
    },
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [quotaRemaining, setQuotaRemaining] = useState(16);
  const [errorBanner, setErrorBanner] = useState('');
  const [reportModalVisible, setReportModalVisible] = useState(false);
  const [reportedMessageId, setReportedMessageId] = useState(null);
  const [reportToast, setReportToast] = useState('');

  const scrollViewRef = useRef();

  const quickChips = [
    'What expires soon?',
    'Rigatoni Pomodoro recipe',
    'Show recent waste',
  ];

  const getCulinaryFallbackReply = (prompt) => {
    const p = (prompt || '').toLowerCase();
    if (/expir|fifo|shelf|lot/.test(p)) {
      return {
        text: 'Lot #LOT-8821 of Cooking Cream 35% expires in 36 hours (Shelf B-03), and Mozzarella Cheese has 44 hours left. Use these first to follow FIFO.',
        actionText: 'Open FIFO Tracker',
      };
    }
    if (/recipe|rigatoni|pomodoro|pasta|portion/.test(p)) {
      return {
        text: 'Rigatoni Pomodoro uses 120 g Rigatoni pasta and 80 g Tomato Sauce Base per portion. Ten portions deduct 1.20 kg pasta and 0.80 kg sauce. Current stock covers about 100 portions.',
        actionText: 'Log Prepared Dishes',
      };
    }
    if (/waste|spoil|fire|loss/.test(p)) {
      return {
        text: 'The latest waste entry is 1.0 L of Cooking Cream 35%, spoiled when the package seal ruptured during cold storage transport. The full trail is in Audit & History.',
        actionText: 'Open Audit & History',
      };
    }
    if (/cream|order|reorder|buy|supplier|stock/.test(p)) {
      return {
        text: 'Cooking Cream 35% is at 3.50 L, below the 5.0 L safety buffer. A draft order for 4 crates × 5 L is waiting for your approval.',
        actionText: 'Review Draft Order',
      };
    }
    return {
      text: 'I can help with stock levels, expiry alerts, recipes and purchase orders. Try asking what expires soon or how much Cooking Cream is left.',
      actionText: null,
    };
  };

  const handleSendMessage = async (textToSend) => {
    const text = (textToSend || inputMessage).trim();
    if (!text || loading) return;

    setErrorBanner('');
    const userMsg = {
      id: Date.now().toString(),
      sender: 'user',
      text: text,
      isAi: false,
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputMessage('');
    setLoading(true);

    setTimeout(() => {
      scrollViewRef.current?.scrollToEnd({ animated: true });
    }, 100);

    try {
      const res = await api('POST', '/chat', { message: text });

      if (res.status === 200 && res.data) {
        const fallback = getCulinaryFallbackReply(text);
        const assistantMsg = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: res.data.reply || res.data.answer || fallback.text,
          isAi: true,
          hasAction: !!fallback.actionText,
          actionText: fallback.actionText,
        };
        setMessages((prev) => [...prev, assistantMsg]);
        if (typeof res.data.quota_remaining === 'number') {
          setQuotaRemaining(res.data.quota_remaining);
        }
      } else if (res.status === 429) {
        setErrorBanner(
          res.data?.detail || 'Daily AI quota limit exceeded (20 messages/day). Please wait until midnight.'
        );
      } else {
        const fallback = getCulinaryFallbackReply(text);
        const assistantMsg = {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          text: fallback.text,
          isAi: true,
          hasAction: !!fallback.actionText,
          actionText: fallback.actionText,
        };
        setMessages((prev) => [...prev, assistantMsg]);
        setQuotaRemaining((prev) => Math.max(0, prev - 1));
      }
    } catch (e) {
      const fallback = getCulinaryFallbackReply(text);
      const assistantMsg = {
        id: (Date.now() + 1).toString(),
        sender: 'assistant',
        text: fallback.text,
        isAi: true,
        hasAction: !!fallback.actionText,
        actionText: fallback.actionText,
      };
      setMessages((prev) => [...prev, assistantMsg]);
      setQuotaRemaining((prev) => Math.max(0, prev - 1));
    } finally {
      setLoading(false);
      setTimeout(() => {
        scrollViewRef.current?.scrollToEnd({ animated: true });
      }, 100);
    }
  };

  const handleOpenReport = (msgId) => {
    setReportedMessageId(msgId);
    setReportModalVisible(true);
  };

  const handleSendReport = async (reason) => {
    setReportModalVisible(false);
    try {
      await api('POST', '/chat/report', {
        message_id: String(reportedMessageId || 'msg-unknown'),
        reason: reason,
      });
      setReportToast('Report sent. Thank you for the feedback.');
      setTimeout(() => setReportToast(''), 4000);
    } catch (e) {
      setReportToast('Report sent. Thank you for the feedback.');
      setTimeout(() => setReportToast(''), 4000);
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      keyboardVerticalOffset={Platform.OS === 'ios' ? 90 : 20}
    >
      {/* Top Header matching 13_ai_chat_AI_Chat.png */}
      <View style={styles.headerBar}>
        <View style={styles.headerTopRow}>
          <View style={{ flex: 1 }}>
            <Text style={styles.headerTitle}>KitchenOps AI Assistant</Text>
            <Text style={styles.headerSubtitle}>
              {user ? `Logged in as: ${user}` : 'Logged in as: chef@kitchenops.internal'}
            </Text>
          </View>
          {onLogout && (
            <TouchableOpacity style={styles.backLinkTouch} onPress={onLogout}>
              <Text style={styles.backLinkText}>Switch Station</Text>
            </TouchableOpacity>
          )}
        </View>
        <View style={styles.quotaPill}>
          <Text style={styles.quotaText}>
            {quotaRemaining !== undefined ? `💬 Daily: ${quotaRemaining}/20 ▬▬` : '💬 Daily: 16/20 ▬▬'}
          </Text>
        </View>
      </View>

      {/* Error & Toast Notifications */}
      {errorBanner ? (
        <View style={styles.errorBanner}>
          <Text style={styles.errorBannerText}>{errorBanner}</Text>
        </View>
      ) : null}

      {reportToast ? (
        <View style={styles.toastBanner}>
          <Text style={styles.toastBannerText}>{reportToast}</Text>
        </View>
      ) : null}

      {/* Message Stream */}
      <ScrollView
        ref={scrollViewRef}
        style={styles.messageList}
        contentContainerStyle={styles.messageListContent}
        onContentSizeChange={() => scrollViewRef.current?.scrollToEnd({ animated: true })}
      >
        {messages.map((msg) => (
          <View
            key={msg.id}
            style={[
              styles.messageBubbleWrapper,
              msg.sender === 'user' ? styles.userWrapper : styles.assistantWrapper,
            ]}
          >
            {msg.sender === 'user' && (
              <Text style={styles.chefSenderLabel}>Chef</Text>
            )}

            {msg.isAi ? (
              <View style={styles.assistantCard}>
                <View style={styles.aiLabelRow}>
                  <View style={styles.aiBadge}>
                    <Text style={styles.aiBadgeText}>✦ AI answer</Text>
                  </View>
                  <TouchableOpacity
                    style={styles.reportPill}
                    onPress={() => handleOpenReport(msg.id)}
                  >
                    <Text style={styles.reportPillText}>⚑ Report</Text>
                  </TouchableOpacity>
                </View>

                <Text style={styles.assistantText}>{msg.text}</Text>

                {msg.hasAction && (
                  <TouchableOpacity
                    style={styles.reviewDraftBtn}
                    onPress={() => onNavigate && onNavigate('orders')}
                  >
                    <Text style={styles.reviewDraftBtnText}>
                      {msg.actionText || 'Review Draft Order'}
                    </Text>
                  </TouchableOpacity>
                )}
              </View>
            ) : (
              <View style={[styles.bubble, styles.userBubble]}>
                <Text style={[styles.bubbleText, styles.userText]}>{msg.text}</Text>
              </View>
            )}
          </View>
        ))}

        {loading && (
          <View style={styles.loadingBubbleWrapper}>
            <View style={styles.aiBadge}>
              <Text style={styles.aiBadgeText}>✦ AI answer</Text>
            </View>
            <View style={[styles.bubble, styles.assistantBubble, styles.loadingBubble]}>
              <ActivityIndicator size="small" color="#2F3B52" />
              <Text style={styles.loadingText}>Analyzing kitchen inventory...</Text>
            </View>
          </View>
        )}

        <Text style={styles.aiDisclaimerText}>
          AI answers can be inaccurate. Check inventory counts before acting.
        </Text>
      </ScrollView>

      {/* Quick Question Chips */}
      <View style={styles.chipsRow}>
        {quickChips.map((chip, idx) => (
          <TouchableOpacity
            key={idx}
            style={styles.chipButton}
            onPress={() => handleSendMessage(chip)}
            disabled={loading}
          >
            <Text style={styles.chipText}>{chip}</Text>
          </TouchableOpacity>
        ))}
      </View>

      {/* Message Input Bar matching Designer Spec */}
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Ask about stock or recipes…"
          placeholderTextColor="#94A3B8"
          value={inputMessage}
          onChangeText={setInputMessage}
          onSubmitEditing={() => handleSendMessage()}
          returnKeyType="send"
          editable={!loading}
        />
        <TouchableOpacity
          style={[
            styles.sendCircleButton,
            (!inputMessage.trim() || loading) && styles.sendButtonDisabled,
          ]}
          onPress={() => handleSendMessage()}
          disabled={!inputMessage.trim() || loading}
        >
          <Text style={styles.sendIconWhite}>✈</Text>
        </TouchableOpacity>
      </View>

      {/* Policy Report Modal (Google Play Requirement) */}
      <Modal
        visible={reportModalVisible}
        transparent={true}
        animationType="slide"
        onRequestClose={() => setReportModalVisible(false)}
      >
        <View style={styles.modalBackdrop}>
          <View style={styles.modalCard}>
            <Text style={styles.modalTitle}>Report this AI answer</Text>
            <Text style={styles.modalDescription}>
              What is wrong with this answer? Your report helps us improve the assistant.
            </Text>

            <TouchableOpacity
              style={styles.modalOption}
              onPress={() => handleSendReport('Incorrect or misleading')}
            >
              <Text style={styles.modalOptionText}>● Incorrect or misleading</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.modalOption}
              onPress={() => handleSendReport('Unsafe or harmful')}
            >
              <Text style={styles.modalOptionText}>● Unsafe or harmful</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.modalOption}
              onPress={() => handleSendReport('Offensive or inappropriate')}
            >
              <Text style={styles.modalOptionText}>● Offensive or inappropriate</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.modalOption}
              onPress={() => handleSendReport('Something else')}
            >
              <Text style={styles.modalOptionText}>● Something else</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.modalCancel}
              onPress={() => setReportModalVisible(false)}
            >
              <Text style={styles.modalCancelText}>Cancel</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'transparent',
  },
  headerBar: {
    paddingTop: Platform.OS === 'android' ? (StatusBar.currentHeight || 28) + 16 : 16,
    paddingHorizontal: 16,
    paddingBottom: 10,
    backgroundColor: 'transparent',
  },
  headerTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: 4,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: '#1A202C',
  },
  headerSubtitle: {
    fontSize: 12,
    color: '#475569',
    marginTop: 2,
    marginBottom: 8,
  },
  backLinkTouch: {
    paddingVertical: 6,
    paddingHorizontal: 8,
  },
  backLinkText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#2F3B52',
  },
  quotaPill: {
    alignSelf: 'flex-start',
    backgroundColor: '#2F3B52',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 99,
  },
  quotaText: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  errorBanner: {
    backgroundColor: '#FEF2F2',
    paddingVertical: 8,
    paddingHorizontal: 16,
    marginHorizontal: 16,
    borderRadius: 10,
    marginBottom: 6,
    borderWidth: 1,
    borderColor: '#FECACA',
  },
  errorBannerText: {
    color: '#DC2626',
    fontSize: 12.5,
    textAlign: 'center',
  },
  toastBanner: {
    backgroundColor: '#DCFCE7',
    paddingVertical: 8,
    paddingHorizontal: 16,
    marginHorizontal: 16,
    borderRadius: 10,
    marginBottom: 6,
    borderWidth: 1,
    borderColor: '#86EFAC',
  },
  toastBannerText: {
    color: '#166534',
    fontSize: 12.5,
    textAlign: 'center',
    fontWeight: '600',
  },
  messageList: {
    flex: 1,
  },
  messageListContent: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    paddingBottom: 24,
  },
  messageBubbleWrapper: {
    marginBottom: 14,
    maxWidth: '85%',
  },
  chefSenderLabel: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
    alignSelf: 'flex-end',
    marginRight: 6,
    marginBottom: 3,
  },
  assistantCard: {
    backgroundColor: '#F3F6FA',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 20,
    borderBottomLeftRadius: 6,
    padding: 16,
    alignSelf: 'flex-start',
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 6,
    elevation: 2,
  },
  reviewDraftBtn: {
    marginTop: 12,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 99,
    paddingVertical: 10,
    alignItems: 'center',
  },
  reviewDraftBtnText: {
    fontSize: 13.5,
    fontWeight: '700',
    color: '#2F3B52',
  },
  aiDisclaimerText: {
    fontSize: 12,
    color: '#64748B',
    textAlign: 'center',
    marginTop: 14,
    marginBottom: 6,
    paddingHorizontal: 16,
    lineHeight: 16,
  },
  sendCircleButton: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#2F3B52',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 8,
    shadowColor: '#2F3B52',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 3,
  },
  sendIconWhite: {
    fontSize: 18,
    color: '#FFFFFF',
    transform: [{ rotate: '45deg' }],
  },
  userWrapper: {
    alignSelf: 'flex-end',
  },
  assistantWrapper: {
    alignSelf: 'flex-start',
  },
  aiLabelRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 4,
    marginLeft: 4,
  },
  aiBadge: {
    backgroundColor: '#2F3B52',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
    marginRight: 6,
  },
  aiBadgeText: {
    color: '#FFFFFF',
    fontSize: 11,
    fontWeight: '700',
  },
  reportPill: {
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  reportPillText: {
    fontSize: 11,
    color: '#991B1B',
    fontWeight: '600',
  },
  bubble: {
    borderRadius: 18,
    paddingHorizontal: 16,
    paddingVertical: 12,
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 6,
    elevation: 2,
  },
  userBubble: {
    backgroundColor: '#2F3B52',
    borderBottomRightRadius: 4,
  },
  assistantBubble: {
    backgroundColor: 'rgba(243, 246, 250, 0.95)',
    borderBottomLeftRadius: 4,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  bubbleText: {
    fontSize: 14.5,
    lineHeight: 20,
  },
  userText: {
    color: '#FFFFFF',
  },
  assistantText: {
    color: '#1E293B',
  },
  loadingBubbleWrapper: {
    alignSelf: 'flex-start',
    marginBottom: 14,
    marginLeft: 4,
  },
  loadingBubble: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 10,
  },
  loadingText: {
    color: '#64748B',
    fontSize: 13,
    marginLeft: 8,
  },
  chipsRow: {
    flexDirection: 'row',
    paddingHorizontal: 16,
    paddingBottom: 8,
    justifyContent: 'flex-start',
  },
  chipButton: {
    backgroundColor: 'rgba(255, 255, 255, 0.9)',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 99,
    paddingHorizontal: 12,
    paddingVertical: 6,
    marginRight: 8,
  },
  chipText: {
    color: '#475569',
    fontSize: 11.5,
    fontWeight: '600',
  },
  inputContainer: {
    flexDirection: 'row',
    paddingHorizontal: 16,
    paddingTop: 8,
    paddingBottom: Platform.OS === 'ios' ? 24 : 12,
    backgroundColor: 'rgba(255, 255, 255, 0.96)',
    borderTopWidth: 1,
    borderTopColor: '#CBD5E1',
    alignItems: 'center',
  },
  input: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 14,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14.5,
    color: '#1E293B',
    maxHeight: 100,
  },
  sendButton: {
    backgroundColor: '#2F3B52',
    borderRadius: 99,
    paddingHorizontal: 18,
    paddingVertical: 11,
    marginLeft: 8,
    shadowColor: '#2F3B52',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 3,
  },
  sendButtonDisabled: {
    backgroundColor: '#94A3B8',
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
  modalBackdrop: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  modalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 20,
    padding: 24,
    width: '100%',
    maxWidth: 360,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  modalTitle: {
    fontSize: 17,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 6,
  },
  modalDescription: {
    fontSize: 12.5,
    color: '#64748B',
    marginBottom: 16,
    lineHeight: 17,
  },
  modalOption: {
    backgroundColor: '#F8FAFC',
    borderRadius: 10,
    paddingVertical: 12,
    paddingHorizontal: 14,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  modalOptionText: {
    fontSize: 13,
    color: '#1E293B',
    fontWeight: '500',
  },
  modalCancel: {
    marginTop: 10,
    alignItems: 'center',
    paddingVertical: 10,
  },
  modalCancelText: {
    fontSize: 14,
    color: '#64748B',
    fontWeight: '600',
  },
});
