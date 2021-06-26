BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "game" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "current_position" INTEGER NOT NULL,
    "deck" INTEGER NOT NULL,
    "canvas" BLOB NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "player" (
    "id" INTEGER NOT NULL UNIQUE,
    "token" TEXT NOT NULL UNIQUE,
    "game_id" INTEGER NOT NULL,
    "position" INTEGER NOT NULL,
    "hand" BLOB NOT NULL,
    "palette" BLOB NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    UNIQUE("position","game_id"),
    FOREIGN KEY("game_id") REFERENCES "game"("id")
);
COMMIT;
