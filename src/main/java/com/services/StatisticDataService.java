package com.services;

import java.sql.Date;
import java.util.List;

import com.model.StatisticData;

public interface StatisticDataService {
	public List<StatisticData> getRawStatisticDataListFromDatetime(Date date, int hour);
	public List<StatisticData> getAveragesData();
	public List<StatisticData> getMostCallTrafficDay();
	public List<StatisticData> getLeastCallTrafficDay();
}
