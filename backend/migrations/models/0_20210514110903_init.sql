-- upgrade --
CREATE TABLE IF NOT EXISTS "adminuser" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_superuser" BOOL NOT NULL  DEFAULT False
);
COMMENT ON COLUMN "adminuser"."password" IS 'Will auto hash with raw password when change';
CREATE TABLE IF NOT EXISTS "language" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "course" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL,
    "description" TEXT NOT NULL,
    "image_link" VARCHAR(200) NOT NULL,
    "author" VARCHAR(80) NOT NULL,
    "estimated_time" INT NOT NULL,
    "language_id" INT NOT NULL REFERENCES "language" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "coursemember" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_sub" VARCHAR(80) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "course_id" INT NOT NULL REFERENCES "course" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_coursemembe_user_su_04babe" ON "coursemember" ("user_sub");
CREATE INDEX IF NOT EXISTS "idx_coursemembe_course__394152" ON "coursemember" ("course_id");
CREATE TABLE IF NOT EXISTS "coursepart" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL,
    "description" TEXT NOT NULL,
    "course_id" INT NOT NULL REFERENCES "course" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_coursepart_course__06308c" ON "coursepart" ("course_id");
CREATE TABLE IF NOT EXISTS "lesson" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL,
    "video" VARCHAR(50) NOT NULL,
    "content" TEXT NOT NULL,
    "course_part_id" INT NOT NULL REFERENCES "coursepart" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_lesson_course__e3e33f" ON "lesson" ("course_part_id");
CREATE TABLE IF NOT EXISTS "lessonviewed" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user_sub" VARCHAR(80) NOT NULL,
    "lesson_id" INT NOT NULL REFERENCES "lesson" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_lessonviewe_user_su_445cd2" ON "lessonviewed" ("user_sub");
CREATE INDEX IF NOT EXISTS "idx_lessonviewe_lesson__c3efe4" ON "lessonviewed" ("lesson_id");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
