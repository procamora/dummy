BEGIN TRANSACTION;
DROP TABLE IF EXISTS "hashes";
CREATE TABLE IF NOT EXISTS "hashes" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"file"	TEXT UNIQUE,
	"hash"	TEXT
);
COMMIT;
