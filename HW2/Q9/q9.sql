/* Question9 */

ALTER TABLE rdata
RENAME COLUMN moment 
TO date;
SELECT * FROM rdata;