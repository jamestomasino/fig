fig
===

Simple web-based Twitter client with regex filtering

### Setup ###

1. Create a sqlite database named web.db in the root folder using the following table structure:

    create table sessions (
        session_id char(128) UNIQUE NOT NULL,
        atime timestamp NOT NULL default current_timestamp,
        data text
    );
