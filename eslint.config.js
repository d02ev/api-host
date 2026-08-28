import js from "@eslint/js";
import prettier from "eslint-config-prettier";

export default [
  {
    ignores: ["dist/", "node_modules/"],
  },
  js.configs.recommended,
  prettier,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        console: "readonly",
        process: "readonly",
        __dirname: "readonly",
      },
    },
    rules: {
      "no-console": "off",
    },
  },
];
