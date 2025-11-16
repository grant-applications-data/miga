-- # Class: ReviewScore Description: Final score or score for a specific criterion, step, and/or reviewer.
--     * Slot: id
--     * Slot: reviewer Description: Anonymized identifier of the reviewer, e.g. R1, R2...
--     * Slot: step Description: Numeric representation of the stage or phase in the grant review process (e.g. "1" for the initial screening, "2" for the panel review...).
--     * Slot: criterion Description: Criterion being evaluated.
--     * Slot: score Description: Numeric score assigned.
-- # Class: GrantApplication Description: Research grant application.
--     * Slot: id
--     * Slot: pi_age Description: Age of the principal investigator.
--     * Slot: pi_gender Description: Gender of the principal investigator.
--     * Slot: application_year Description: Year the application was submitted, or year the grant scheme was published.
--     * Slot: grant_scheme Description: The funding scheme under which the grant was applied.
--     * Slot: discipline Description: Organizational division (panel, directorate, office...) that represents the discipline of the application. The most granular division should always be preferred.
--     * Slot: success Description: Whether the application was successful.
-- # Class: GrantApplication_scores
--     * Slot: GrantApplication_id Description: Autocreated FK slot
--     * Slot: scores_id Description: One or more scores assigned during the review process. A single score can be interpreted as the final score.

CREATE TABLE "ReviewScore" (
	id INTEGER NOT NULL,
	reviewer TEXT,
	step INTEGER,
	criterion TEXT,
	score FLOAT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ReviewScore_id" ON "ReviewScore" (id);
CREATE TABLE "GrantApplication" (
	id INTEGER NOT NULL,
	pi_age INTEGER,
	pi_gender TEXT,
	application_year INTEGER,
	grant_scheme TEXT,
	discipline TEXT,
	success BOOLEAN,
	PRIMARY KEY (id)
);CREATE INDEX "ix_GrantApplication_id" ON "GrantApplication" (id);
CREATE TABLE "GrantApplication_scores" (
	"GrantApplication_id" INTEGER,
	scores_id INTEGER,
	PRIMARY KEY ("GrantApplication_id", scores_id),
	FOREIGN KEY("GrantApplication_id") REFERENCES "GrantApplication" (id),
	FOREIGN KEY(scores_id) REFERENCES "ReviewScore" (id)
);CREATE INDEX "ix_GrantApplication_scores_scores_id" ON "GrantApplication_scores" (scores_id);CREATE INDEX "ix_GrantApplication_scores_GrantApplication_id" ON "GrantApplication_scores" ("GrantApplication_id");

