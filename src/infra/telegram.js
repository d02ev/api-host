import TelegramBot from 'node-telegram-bot-api';

export const createTelegram = config => {
    return new TelegramBot(config.token, { polling: false });
};