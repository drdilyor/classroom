-- upgrade --
CREATE TABLE IF NOT EXISTS "author" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(80) NOT NULL
);;
ALTER TABLE "course" ADD "author_id" INT;
INSERT INTO "author" ("name") SELECT "author" FROM "course";
UPDATE "course" set "author_id" = "author"."id" from "author" where "course"."author" = "author"."name";
ALTER TABLE "course" DROP COLUMN "author";
ALTER TABLE "course" ADD CONSTRAINT "fk_course_author_32d21668" FOREIGN KEY ("author_id") REFERENCES "author" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "course" DROP CONSTRAINT "fk_course_author_32d21668";
ALTER TABLE "course" ADD "author" VARCHAR(80) NULL;
UPDATE course SET author = a.name from author a where a.id = course.author_id;
ALTER TABLE "course" ALTER COLUMN "author" SET NOT NULL;
ALTER TABLE "course" DROP COLUMN "author_id";
DROP TABLE IF EXISTS "author";
