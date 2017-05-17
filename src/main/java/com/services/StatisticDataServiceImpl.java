package com.services;

import java.sql.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.daos.StatisticDataDao;
import com.model.StatisticData;

@Service
public class StatisticDataServiceImpl implements StatisticDataService {
	private StatisticDataDao statisticDataDao;

	@Autowired
	public void setStatisticDataDao(StatisticDataDao statisticDataDao) {
		this.statisticDataDao = statisticDataDao;
	}

	@Override
	public List<StatisticData> getStatisticDataList(Date date, int hour) {
		return statisticDataDao.getStatisticDataList(date, hour);
	}
}
