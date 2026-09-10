import { Bot } from 'grammy';

export const createTelegram = (config) => {
  return new Bot(config.token);
};
