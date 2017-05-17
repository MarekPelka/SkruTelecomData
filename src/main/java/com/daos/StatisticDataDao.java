package com.daos;

import java.sql.Date;
import java.util.List;

import com.model.StatisticData;

public interface StatisticDataDao {
	public List<StatisticData> getStatisticDataList(Date date, int hour);
}
