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
@RequestMapping("/data")
public class StatisticDataController {
	private StatisticDataService statisticDataService;

	@Autowired(required = true)
	public void setStatisticDataService(StatisticDataService statisticDataService) {
		this.statisticDataService = statisticDataService;
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.GET)
	public String choose(Model model) {
		model.addAttribute("selectionData", new SelectionData());
		return "chooser";
	}

	@RequestMapping(value = "/chooser", method = RequestMethod.POST)
	public ModelAndView choose(@ModelAttribute("selectionData") SelectionData selectionData) {
		List<StatisticData> resultList = new ArrayList<>();

		SimpleDateFormat format = new SimpleDateFormat("MM/dd/yyyy");
		java.util.Date date = null;
		try {
			date = format.parse(selectionData.getDataDate());
			// java.util.Date newDate = DateUtils.addMonths(date, 1);
			java.sql.Date sqlDate = new java.sql.Date(date.getTime());
			int hour = Integer.parseInt(selectionData.getDataTime());
			resultList = statisticDataService.getStatisticDataList(sqlDate, hour);

		} catch (ParseException e) {
			System.err.println("Parse exception in controller:" + e.getMessage());
		}
		

		ModelAndView model = new ModelAndView("main");

		List<Double> valueList = new ArrayList<>();
		for (int i = 0; i < 10000; i++) {
			valueList.add(0.0);
		}

		switch (selectionData.getWhichData()) {
		case "smsin":
			for (int i = 0; i < 10000; i++) {
				valueList.set(resultList.get(i).getSquareId() - 1, resultList.get(i).getSmsIn());
			}
			break;
		case "smsout":
			for (int i = 0; i < 10000; i++) {
				valueList.set(resultList.get(i).getSquareId() - 1, resultList.get(i).getSmsOut());
			}
			break;
		case "callin":
			for (int i = 0; i < 10000; i++) {
				valueList.set(resultList.get(i).getSquareId() - 1, resultList.get(i).getCallIn());
			}
			break;
		case "callout":
			for (int i = 0; i < 10000; i++) {
				valueList.set(resultList.get(i).getSquareId() - 1, resultList.get(i).getCallOut());
			}
			break;
		case "internettraffic":
			for (int i = 0; i < 10000; i++) {
				valueList.set(resultList.get(i).getSquareId() - 1, resultList.get(i).getInternetTraffic());
			}
			break;
		default:
			break;
		}
		model.addObject("valueList", valueList);
		return model;
	}

	@RequestMapping(value = "/main", method = RequestMethod.GET)
	public String getMain() {
		return "main";
	}
	
	@RequestMapping(value = "/proceeded", method = RequestMethod.GET)
	public String getProceeded() {
		return "proceeded";
	}
	
	@RequestMapping(value = "/table", method = RequestMethod.GET)
	public String getTable() {
		return "table";
	}

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String getIndex() {
		return "redirect:index.jsp";
	}

}
