package com.controllers;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.model.SelectionData;
import com.model.StatisticData;
import com.services.StatisticDataService;

@Controller
@RequestMapping("/rawdata")
public class RawDataController {
	private StatisticDataService statisticDataService;

	@Autowired(required = true)
	public void setStatisticDataService(StatisticDataService statisticDataService) {
		this.statisticDataService = statisticDataService;
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.GET)
	public String choose(Model model) {
		model.addAttribute("selectionData", new SelectionData());
		return "rawchooser";
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.POST)
	public ModelAndView choose(@ModelAttribute("selectionData") SelectionData selectionData) {
		ModelAndView model = new ModelAndView("maprenderer");
		
		List<StatisticData> allRawData = new ArrayList<>();

		SimpleDateFormat format = new SimpleDateFormat("MM/dd/yyyy");
		java.util.Date date = null;
		try {
			date = format.parse(selectionData.getDataDate());
			// java.util.Date newDate = DateUtils.addMonths(date, 1);
			java.sql.Date sqlDate = new java.sql.Date(date.getTime());
			int hour = Integer.parseInt(selectionData.getDataTime());
			allRawData = statisticDataService.getRawStatisticDataListFromDatetime(sqlDate, hour);

		} catch (ParseException e) {
			System.err.println("Parse exception in controller:" + e.getMessage());
		}

		

		List<Double> valueList = new ArrayList<>();
		for (int i = 0; i < 10000; i++) {
			valueList.add(0.0);
		}

		switch (selectionData.getWhichData()) {
		case "smsin":
			for (int i = 0; i < 10000; i++) {
				valueList.set(allRawData.get(i).getSquareId() - 1, allRawData.get(i).getSmsIn());
			}
			break;
		case "smsout":
			for (int i = 0; i < 10000; i++) {
				valueList.set(allRawData.get(i).getSquareId() - 1, allRawData.get(i).getSmsOut());
			}
			break;
		case "callin":
			for (int i = 0; i < 10000; i++) {
				valueList.set(allRawData.get(i).getSquareId() - 1, allRawData.get(i).getCallIn());
			}
			break;
		case "callout":
			for (int i = 0; i < 10000; i++) {
				valueList.set(allRawData.get(i).getSquareId() - 1, allRawData.get(i).getCallOut());
			}
			break;
		case "internettraffic":
			for (int i = 0; i < 10000; i++) {
				valueList.set(allRawData.get(i).getSquareId() - 1, allRawData.get(i).getInternetTraffic());
			}
			break;
		default:
			break;
		}
		model.addObject("valueList", valueList);
		return model;
	}
}
