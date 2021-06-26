BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "game" (
    "id" INTEGER NOT NULL UNIQUE,
    "current_position" INTEGER NOT NULL,
    "deck" TEXT NOT NULL,
    "canvas" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "player" (
    "id" INTEGER NOT NULL UNIQUE,
    "game_id" INTEGER NOT NULL,
    "position" INTEGER NOT NULL,
    "hand" TEXT NOT NULL,
    "palette" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    UNIQUE("position","game_id"),
    FOREIGN KEY("game_id") REFERENCES "game"("id")
);
CREATE TABLE IF NOT EXISTS "session" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "game_id" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("game_id") REFERENCES "game"("id")
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "session_id" INTEGER NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("session_id") REFERENCES "session"("id")
);
COMMIT;
