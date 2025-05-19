### Day1 Starts (18th May 2025)<br>
<br>
** What I studied **<br>
-Revised Python Basics<br>
-Revised SQL <br>
-Studied about Git, Github<br>
-Made my Github account, make some small progress and learning in Git and Github<br>
<br>
** What I coded **<br>
-Made Stone-Paper-Scissors Game for warmup<br>
<br>
<br>
------------------------------------------------------------------------------------------------------------------------<br>
<br>
<br>
### Day 2 — PostgreSQL setup<br>
<br>
**Goals set**<br>
- Stand up a dedicated project database (`order_bot`)<br>
- Create a least-privilege login (`ob_user`)<br>
- Load schema + seed data from an external script<br>
- Verify everything through pgAdmin and psql<br>
<br>
**What I actually did**<br>
1. Fixed PATH so `psql --version` works.<br>
2. Started PostgreSQL service; connected as super-user `postgres`.<br>
3. Ran:<br>
   - CREATE DATABASE order_bot;<br>
   - CREATE USER ob_user WITH PASSWORD ‘ob_pass’;<br>
   - GRANT ALL PRIVILEGES ON DATABASE order_bot TO ob_user;<br>
4. Granted schema rights inside `order_bot`  <br>
   `GRANT CREATE,USAGE ON SCHEMA public TO ob_user;`<br>
5. Wrote **init_db.sql** containing tables `orders` and `progress_events` plus 5 mock orders.<br>
6. Executed the script as **ob_user** — confirmed messages:  <br>
   `CREATE TABLE`, `INSERT 0 5`, `INSERT 0 2`.<br>
7. In pgAdmin: refreshed tree → Tables now show `orders`, `progress_events`.<br>
8. Browsed data: 5 rows in `orders`, 2 events linked to order 1.<br>
9. Committed `init_db.sql` to GitHub.  <br>
10. Added this diary entry.<br>

**Problems / fixes**<br>
- *psql not recognized*: solved by adding `C:\Program Files\PostgreSQL\17\bin` to PATH.  <br>
- *permission denied for schema public*: fixed with the GRANT CREATE/USAGE commands.  <br>
- pgAdmin tree didn’t show new tables until I hit **Refresh**.<br>

**Key take-aways**<br>
- Database privilege model is two-layer: database (CONNECT) vs schema (CREATE).  <br>
- Keeping schema scripts in Git makes DB reproducible.  <br>
- `DROP TABLE IF EXISTS …` lets scripts be rerun safely.<br>
<br>
**Next up (Day 3)**<br>
- Set up Python virtualenv.<br>
- Install SQLAlchemy + psycopg2.<br>
- Map `orders` and `progress_events` to ORM classes.<br>
- Write a unit test for `get_order_status(order_id)`.<br>
<br>
--------------------------------------------------------------------------------------------------------------------------------<br>




