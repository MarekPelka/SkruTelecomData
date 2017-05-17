package com.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class StatisticData {
	@Id
	@Column(name = "SQUARE_ID", nullable = false)
	private Integer squareId;
	@Column(name = "SMS_IN", nullable = true)
	private Double smsIn;
	@Column(name = "SMS_OUT", nullable = true)
	private Double smsOut;
	@Column(name = "CALL_IN", nullable = true)
	private Double callIn;
	@Column(name = "CALL_OUT", nullable = true)
	private Double callOut;
	@Column(name = "INTERNET_TRAFFIC", nullable = true)
	private Double internetTraffic;

	public Integer getSquareId() {
		return squareId;
	}

	public void setSquareId(Integer squareId) {
		this.squareId = squareId;
	}

	public Double getSmsIn() {
		return smsIn;
	}

	public void setSmsIn(Double smsIn) {
		this.smsIn = smsIn;
	}

	public Double getSmsOut() {
		return smsOut;
	}

	public void setSmsOut(Double smsOut) {
		this.smsOut = smsOut;
	}

	public Double getCallIn() {
		return callIn;
	}

	public void setCallIn(Double callIn) {
		this.callIn = callIn;
	}

	public Double getCallOut() {
		return callOut;
	}

	public void setCallOut(Double callOut) {
		this.callOut = callOut;
	}

	public Double getInternetTraffic() {
		return internetTraffic;
	}

	public void setInternetTraffic(Double internetTraffic) {
		this.internetTraffic = internetTraffic;
	}

	@Override
	public String toString() {
		return "StatisticData [squareId=" + squareId + ", smsIn=" + smsIn + ", smsOut="
				+ smsOut + ", callIn=" + callIn + ", callOut=" + callOut + ", internetTraffic=" + internetTraffic + "]";
	}
	
	

}
