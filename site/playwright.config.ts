import { defineConfig, devices } from '@playwright/test';

// Testy chodzą po zbudowanej stronie (astro preview), nie po serwerze deweloperskim:
// sprawdzamy dokładnie to, co trafi na GitHub Pages. Osobny port, żeby nie gryzł się z `npm run dev`.
const PORT = 4322;
const CI = !!process.env.CI;

export default defineConfig({
  testDir: 'tests',
  fullyParallel: true,
  forbidOnly: CI,
  retries: CI ? 1 : 0,
  reporter: CI ? [['github'], ['html', { open: 'never' }]] : 'list',
  use: {
    baseURL: `http://localhost:${PORT}`,
    trace: 'retain-on-failure',
  },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
  webServer: {
    command: `npm run preview -- --port ${PORT}`,
    url: `http://localhost:${PORT}`,
    reuseExistingServer: !CI,
  },
});
