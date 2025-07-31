default_sql = """WITH tag_view AS (
    SELECT 
        fsportal_mst_tag_table.tag_id AS tag_id,
        fsportal_mst_tag_table.tag AS tag,
        fsportal_notice_tag_table.notice_id
    FROM fsportal_mst_tag_table
    LEFT OUTER JOIN fsportal_notice_tag_table 
    ON fsportal_mst_tag_table.tag_id = fsportal_notice_tag_table.tag_id
),
Allsearch AS (
    SELECT 
        fsportal_notice_table.notice_id AS notice_id,
        fsportal_notice_table.title AS title,
        fsportal_notice_table.content AS content,
        fsportal_notice_table.registration_date AS registration_date,
        fsportal_notice_table.user_name AS user_name,
        fsportal_notice_table.publication_start AS publication_start,
        fsportal_notice_table.publication_end AS publication_end,
        LISTAGG(tag_view.tag_id, ',') WITHIN GROUP (ORDER BY tag_view.tag_id) AS tag_id,
        LISTAGG(tag_view.tag, ',') WITHIN GROUP (ORDER BY tag_view.tag) AS tag
    FROM fsportal_notice_table
    LEFT OUTER JOIN tag_view 
    ON fsportal_notice_table.notice_id = tag_view.notice_id
    GROUP BY 
        fsportal_notice_table.notice_id,
        fsportal_notice_table.title,
        fsportal_notice_table.content,
        fsportal_notice_table.registration_date,
        fsportal_notice_table.user_name,
        fsportal_notice_table.publication_start,
        fsportal_notice_table.publication_end
)
SELECT 
    notice_id,
    title,
    content,
    registration_date,
    user_name,
    publication_start,
    publication_end,
    tag
FROM Allsearch
"""

master_sql = """SELECT * FROM fsportal_mst_tag_table WHERE """

db_col = [
    "notice_id",
    "title",
    "content",
    "registration_date",
    "user_name",
    "publication_start",
    "publication_end",
    "tag",
]

error_result400_1 = {
    "statuscode": 400,
    "body": "入力値が不正です。",
}
error_result400_2 = {
    "statuscode": 400,
    "body": "該当するタグが存在しません。",
}
error_result500_1 = {
    "statuscode": 500,
    "body": "データベースでエラーが起きました。",
}
error_result500_2 = {
    "statuscode": 500,
    "body": "システム管理者（fs-ikusei@ml.toyotasystems.com）へご連絡ください。",
}