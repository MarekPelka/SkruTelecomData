package com.daos;

import java.sql.Date;
import java.util.List;

import com.model.StatisticData;

public interface StatisticDataDao {
	public List<StatisticData> getRawDataListFromDatetime(Date date, int hour);
	public List<StatisticData> getAveragesData();
	public List<StatisticData> getMostCallTrafficDay();
	public List<StatisticData> getLeastCallTrafficDay();
}
