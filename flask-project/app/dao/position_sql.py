do_sql={
    "searchPosition":"SELECT * from position_info",
     "select_position":"SELECT position.* FROM company LEFT JOIN position on company.id=position.company_id WHERE company.name like '%{0}%'",
    "select_id":"SELECT * FROM  position  WHERE id={0}",
    "searchProfession":"select * from profession",
    "searchPositionByName":"select * from position_info where name like '%{0}%' or city_name like '%{1}%'",
    "searchPositionById":"select po.*,position.job_nature,position.attraction,position.tags from position INNER JOIN position_info as po ON position.id=po.id WHERE po.id={0}"
}