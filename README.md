Automydumper handles backups, retention and rotation for MySQL, Percona Server and Mariadb servers. It uses Mydumper under the hood.

### Configuring Automydumper

Overriding defaults should be done in ~/.automydumper.cfg or /etc/automydumper.cfg, in that order. 

### Running Automydumper

Running 'automydumper' ( or waiting for the cron ) is all you need to do to get an actual backup.

### Flexible backup directories

By default, backups are placed in /var/backups/automydumper/YYYY-mm-dd.

You can however change the destination by changing the backup_dir_format variable in /etc/automydumper.cfg.

Note: Only letters (both lower and upper case), numbers, dashes and underscores are allowed once the date has been formatted!

Formats can be tested by supplying your format to the date command. Eg. `date +%F` 

### Logs

A log file is stored inside the backup directory. It's called automydumper.log.

### Running scripts before and after the actual backup

You can specify a pre_dir (default /usr/share/automydumper/pre.d) and post_dir (default /usr/share/automydumper/post.d).
Any executable files present in those directories will either be run before the backup (pre_dir) or afterwards (post_dir).
Scripts can be named anything, they just have to be executable by the user in order to be executed by Automydumper.

By default scripts are only executed as long is nothing fails. 
As soon as the backup (or a previously executed pre or post script) fails, everything else is skipped. This can however be tweaked by adding labels to your scripts.

#### Script labels

You can provide a couple of labels to steer the running of your scripts.

Add the following string anywhere in your code for them to take effect:

`automydumper:run:on-error-only`

Script will only run if something has gone wrong and the backup isn't successful. Handy to gather some debugging info for example.

`automydumper:run:always`

Script will be executed no matter the outcome of the backup, so both on failure and success. Handy for alerting/monitoring for example.

#### Script variables

A few environment variables are exported for use in your pre and post scripts.

`AUTOMYDUMPER_BACKUP_DIR`
`AUTOMYDUMPER_BACKUP_ROOT`
`AUTOMYDUMPER_CFG_FILE`
`AUTOMYDUMPER_EXIT_CODE`
`AUTOMYDUMPER_EXIT_MESSAGE`

### Restoring backups

Restoring backups can be done either with myloader ( part of the mydumper package ), or by manually zcat'ing a table backup to mysql.
Please refer to the myloader man page for more details. Below are some of the mostly-used use-cases.

##### Restoring a full MySQL instance ( all databases, all tables ), overwriting existing tables:

myloader -d /var/backups/automydumper/2017-12-31 -o -v 3

##### Restoring a single database (db1), overwriting existing tables:

myloader -d /var/backups/automydumper/2017-12-31 -o -v 3 -s db1

##### Restoring a single table 't1' from database db1:

zcat /var/backups/automydumper/2017-12-31/db1.t1.sql.gz | mysql db1
