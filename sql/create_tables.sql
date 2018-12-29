-- TABLE REPOSITORIES
CREATE TABLE `repositories` (
	`id`	INTEGER,
	`name`	TEXT ( 250 ),
	`full_name`	TEXT ( 250 ),
	`description`	TEXT ( 250 ),
	`homepage`	TEXT ( 250 ),
	`git_url`	TEXT ( 250 ),
	`ssh_url`	TEXT ( 250 ),
	`language`	TEXT ( 25 ),
	`private`	TEXT ( 5 ),
	`archived`	TEXT ( 5 ),
	`forks_count`	INTEGER,
	`open_issues_count`	INTEGER,
	`score`	INTEGER,
	`size`	INTEGER,
	`stargazers_count`	INTEGER,
	`watchers_count`	INTEGER
);
