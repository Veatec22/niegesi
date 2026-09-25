# Jedno konto, logowanie linkiem na e-mail

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Pracownia ma jedno konto, logowane linkiem z Supabase Auth wysyłanym na e-mail
administratora. Rejestracja jest wyłączona. Reguły RLS przepuszczają tylko jego `user_id`,
a każda Edge Function sprawdza to samo. Na start najprostsza droga; logowanie
przez GitHub OAuth wymaga własnej aplikacji OAuth, a dla jednej osoby nic nie daje.
