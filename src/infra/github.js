import { Octokit } from "octokit";

export const createGithub = (config) => {
  return new Octokit({ auth: config.token });
};
