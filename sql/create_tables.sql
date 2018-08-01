-- TABLE REPOSITORIES
CREATE TABLE repositories (
	'id' INTEGER NOT NULL,
	'name' TEXT(250),
	'full_name' TEXT(250),
	'description' TEXT(250),
	'homepage' TEXT(250),
	'git_url' TEXT(250),
	'ssh_url' TEXT(250),
	'language' TEXT(25),
	'private' TEXT(5),
	'archived' TEXT(5)
);
