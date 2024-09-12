import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,
  ...tseslint.configs.stylisticTypeChecked,
  {
    languageOptions: {
      parserOptions: {
        project: true,
      },
    },
  },
  {
    ignores: [
      "node_modules/*",
      ".git/*",
      ".gitignore",
      "**/bun.lockb",
      "vite.config.ts.*",
      "vite.config.js.*",
      "dist/*",
      "eslint.config.js",
    ],
  },
);
