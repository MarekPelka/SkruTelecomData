<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<html>
<head>
<title>Chooser page</title>
<link href="<c:url value='/css/bootstrap.css' />" rel="stylesheet"></link>
<link href="<c:url value='/css/app.css' />" rel="stylesheet"></link>
<link rel="stylesheet" type="text/css"
	href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.2.0/css/font-awesome.css" />
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script>
	$(function() {
		$("#datepicker").datepicker();
	});
</script>
<style>
h1 {
	color: white;
	font-family: 'Helvetica Neue', sans-serif;
	font-size: 46px;
	font-weight: 100;
	line-height: 50px;
	letter-spacing: 1px;
	padding: 0 0 5px;
	border-bottom: double #555;
}
</style>
</head>
<body>
	<c:url var="chooseAction" value="/rawdata/chooser"></c:url>
	<div id="mainWrapper">
		<div class="my-container">
			<div class="my-card">
				<div class="my-form">
					<form:form action="${chooseAction}" method="post"
						class="form-horizontal" commandName="selectionData">
						<div align="center">
							<h1>SKRU PROJECT</h1>
						</div>
						<div class="input-group input-sm">
							<label class="input-group-addon" for=dataDate> <i
								class="fa fa-calendar"></i>
							</label>
							<form:input path="dataDate" value="11/01/2013" type="text"
								class="form-control" id="datepicker" placeholder="Enter date" />
						</div>
						<div class="input-group input-sm">
							<label class="input-group-addon" for=dataTime> <i
								class="fa fa-clock-o"></i>
							</label>
							<form:input path="dataTime" type="number" min="1" max="31"
								class="form-control" placeholder="Enter Hour" />
						</div>
						<div class="input-group input-sm">
							<label class="input-group-addon" for=whichData> <i
								class="fa fa-clock-o"></i>
							</label>
							<form:radiobutton path="whichData" value="smsin" />
							SmS In<br/>
							<form:radiobutton path="whichData" value="smsout" />
							SmS Out<br/>
							<form:radiobutton path="whichData" value="callin" />
							Call In<br/>
							<form:radiobutton path="whichData" value="callout" />
							Call Out<br/>
							<form:radiobutton path="whichData" value="internettraffic" />
							Internet Traffic<br/>
						</div>
						<div class="form-actions">
							<input type="submit"
								class="btn btn-block btn-primary btn-default"
								value="Take a look!">
						</div>
					</form:form>
				</div>
			</div>
		</div>
	</div>


</body>
</html>