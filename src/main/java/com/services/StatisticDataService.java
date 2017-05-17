package com.services;

import java.sql.Date;
import java.util.List;

import com.model.StatisticData;

public interface StatisticDataService {
	public List<StatisticData> getStatisticDataList(Date date, int hour);
}
