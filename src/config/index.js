import { configDotenv } from 'dotenv';

configDotenv();

const required = (name) => {
  const value = process.env[name];

  if (!value) throw new Error(`Missing required environment variable: ${name}`);

  return value;
};

export const config = {
  port: process.env.PORT || 3000,
  supabase: {
    projectUrl: required("SUPABASE_PROJECT_URL"),
    serviceRoleKey: required("SUPABASE_SERVICE_ROLE_KEY"),
    anonKey: required("SUPABASE_ANON_KEY"),
  },
  github: {
    token: required("GITHUB_PAT"),
    owner: required("GITHUB_OWNER"),
    repo: required("GITHUB_REPO"),
    workflowPath: required("GITHUB_WORKFLOW_PATH"),
  },
  telegram: {
    chatId: required("TELEGRAM_CHAT_ID"),
    token: required("TELEGRAM_BOT_TOKEN"),
  },
};
