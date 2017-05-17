package com.daos;

import java.sql.Date;
import java.text.SimpleDateFormat;
import java.util.List;
import java.util.stream.Collectors;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import com.model.StatisticData;

@Repository
@Transactional
public class StatisticDataDaoImpl implements StatisticDataDao {
	private SessionFactory sessionFactory;

	@Autowired
	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
	
	@Override
	public List<StatisticData> getStatisticDataList(Date date, int hour) {
		Session session = sessionFactory.getCurrentSession();
		Transaction tx = session.beginTransaction();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MMM-dd--");
		List<StatisticData> dataList = sessionFactory.getCurrentSession().createNativeQuery(
				"SELECT square_id, AVG(sms_in) as sms_in, AVG(sms_out) as sms_out, AVG(call_in) as call_in, AVG(call_out) as call_out,"
				+ " AVG(internet_traffic) as internet_traffic "
				+ "FROM `milano_converted_"+sdf.format(date).toLowerCase()+String.format("%02d", hour)+"` GROUP BY SQUARE_ID",StatisticData.class
				).list();
		
		tx.commit();
		return dataList;
	}

}
