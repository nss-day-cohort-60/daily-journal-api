CREATE TABLE `Entries`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `timestamp` CURRENT_DATE NOT NULL,
    `concepts` NVARCHAR(50)  NOT NULL,
    `journal_entry` TEXT NOT NULL,
    `user_id` INTEGER NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Users`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` NVARCHAR(20) NOT NULL,
    `email` NVARCHAR(50) NOT NULL
);

CREATE TABLE `Moods`
(
    `id` INTEGER NOT NULL PRIMARY KEY,
    `label` NVARCHAR(25) NOT NULL
);

CREATE TABLE `Tags`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `subject` NVARCHAR(160) NOT NULL
);

CREATE TABLE `Entry_Tags`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id` INTEGER NOT NULL,
    `tag_id` INTEGER NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

INSERT INTO `Entries` VALUES (1, 1614659931683, 'javascript', 'this post is about javascript', 1, 2);
INSERT INTO `Entries` VALUES (2, 1614659931684, 'python', 'this is about python', 2, 1);
INSERT INTO `Entries` VALUES (3, 1614659931685, 'react', 'birds are not real', 3, 3);
INSERT INTO `Entries` VALUES (4, 1614659931686, 'conspiracy', 'if birds are real, prove it', 4, 2);
INSERT INTO `Entries` VALUES (5, 1614659931687, 'aliens', 'the truth is out there', 5, 1);

INSERT INTO `Users` VALUES (null, 'Coach', 'coach_steve@DeVryUniversity.edu');
INSERT INTO `Users` VALUES (null, 'Kanye', 'kanye@kanye.com/kanye');
INSERT INTO `Users` VALUES (null, 'Sydney', 'land_of_ooo@adventuretime.com');
INSERT INTO `Users` VALUES (null, 'Dakota', 'hellyeahbrother@ohyeah.com');
INSERT INTO `Users` VALUES (null, 'Taylor', 'ihatekanye@vmaawards.com');

INSERT INTO `Moods` VALUES (1, 'Sad');
INSERT INTO `Moods` VALUES (2, 'Ok');
INSERT INTO `Moods` VALUES (3, 'Happy');

INSERT INTO `Tags` VALUES (null, 'javascript');
INSERT INTO `Tags` VALUES (null, 'python');
INSERT INTO `Tags` VALUES (null, 'react');
INSERT INTO `Tags` VALUES (null, 'conspiracy');
INSERT INTO `Tags` VALUES (null, 'aliens');

INSERT INTO `Entry_Tags` VALUES (null, 1, 1);
INSERT INTO `Entry_Tags` VALUES (null, 2, 2);
INSERT INTO `Entry_Tags` VALUES (null, 3, 3);
INSERT INTO `Entry_Tags` VALUES (null, 4, 4);
<<<<<<< HEAD
INSERT INTO `Entry_Tags` VALUES (null, 5, 5);
=======
INSERT INTO `Entry_Tags` VALUES (null, 5, 5);

DROP TABLE Users 

SELECT
            e.id,
            e.timestamp,
            e.concepts,
            e.journal_entry,
            e.user_id,
            e.mood_id,
            et.id,
            et.entry_id,
            et.tag_id,
            t.id,
            t.subject
        FROM Entry_tags et
        JOIN entries e
            ON e.id = et.entry_id
        JOIN Tags t 
            ON t.id = et.tag_id
>>>>>>> main
