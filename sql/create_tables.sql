-- TABLE REPOSITORIES [SQLITE]
CREATE TABLE `repositories` (
	`id`				TEXT (25),
	`name`				TEXT (250),
	`full_name`			TEXT (250),
	`description`		TEXT (250),
	`homepage`			TEXT (250),
	`git_url`			TEXT (250),
	`ssh_url`			TEXT (250),
	`language`			TEXT (25),
	`private`			TEXT (5),
	`archived`			TEXT (5),
	`forks_count`		INTEGER,
	`open_issues_count`	INTEGER,
	`score`				INTEGER,
	`size`				INTEGER,
	`stargazers_count`	INTEGER,
	`watchers_count`	INTEGER
);

-- TABLE REPOSITORIES [POSTGRES]
CREATE TABLE repositories (
	id					TEXT,
	name_				TEXT,
	full_name			TEXT,
	description			TEXT,
	homepage			TEXT,
	git_url				TEXT,
	ssh_url				TEXT,
	language_			TEXT,
	private				TEXT,
	archived			TEXT,
	forks_count			INTEGER,
	open_issues_count	INTEGER,
	score				INTEGER,
	size_				INTEGER,
	stargazers_count	INTEGER,
	watchers_count		INTEGER
);