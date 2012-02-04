# @INVIENT_COPYRIGHT@
# @MUNTJAC_LICENSE@

"""Window for Invient charts demo."""


class InvientChartsDemoWin(Window):
    _mainSplit = None
    _leftLayout = None
    _rightLayout = None
    _navTree = None
    _eventLog = TextArea()
    _TREE_ITEM_CAPTION_PROP_ID = 'ChartType'

    def __init__(self):
        mainLayout = VerticalLayout()
        self.setContent(mainLayout)
        self.setSizeFull()
        mainLayout.setSizeFull()
        self.setCaption('Invient Charts')
        infoBar = HorizontalLayout()
        mainLayout.addComponent(infoBar)
        infoBar.setHeight('50px')
        infoBar.setWidth('100%')
        lblAppTitle = Label('Demo Gallery for Invient Charts')
        lblAppTitle.setSizeFull()
        lblAppTitle.setStyleName('v-label-app-title')
        infoBar.addComponent(lblAppTitle)
        self._mainSplit = HorizontalSplitPanel()
        self._mainSplit.setSizeFull()
        mainLayout.addComponent(self._mainSplit)
        mainLayout.setExpandRatio(self._mainSplit, 1)
        self._leftLayout = VerticalLayout()
        self._leftLayout.setSpacing(True)
        self._mainSplit.setFirstComponent(self._leftLayout)
        self._rightLayout = VerticalLayout()
        self._rightLayout.setSpacing(True)
        self._rightLayout.setMargin(True)
        self._mainSplit.setSecondComponent(self._rightLayout)
        self._mainSplit.setSplitPosition(200, Sizeable.UNITS_PIXELS)
        self._navTree = self.createChartsTree()
        self._leftLayout.addComponent(self._navTree)
        self._eventLog.setReadOnly(True)
        self._eventLog.setStyleName('v-textarea-chart-events-log')
        self._eventLog.setSizeFull()
        self._eventLog.setHeight('200px')
        self.setTheme('chartdemo')

    def attach(self):
        super(InvientChartsDemoWin, self).attach()
        self._isAppRunningOnGAE = self.getInvientChartsDemoApp().isAppRunningOnGAE()
        # Select line chart when the screen is loaded
        self._navTree.select(self.DemoSeriesType.LINE.getName() + self._SEPARATOR + self.ChartName.BASIC.getName())

    _isAppRunningOnGAE = None

    def isAppRunningOnGAE(self):
        return self._isAppRunningOnGAE

    def getInvientChartsDemoApp(self):
        return self.getApplication()

    def showChart(self, demoSeriesTypeName, chartNameString):
        if not self._isAppRunningOnGAE:
            self.stopSplineSelfUpdateThread()
        demoSeriesType = self.getDemoSeriesType(demoSeriesTypeName)
        chartName = self.getChartName(chartNameString)
        if demoSeriesType is not None and chartName is not None:
            _0 = demoSeriesType
            _1 = False
            while True:
                if _0 == self.COMBINATION:
                    _1 = True
                    _2 = chartName
                    _3 = False
                    while True:
                        if _2 == self.COMBINATION_COLUMN_LINE_AND_PIE:
                            _3 = True
                            self.showCombination()
                            break
                        if (_3 is True) or (_2 == self.SCATTER_WITH_REGRESSION_LINE):
                            _3 = True
                            self.showCombinationScatterWithRegressionLine()
                            break
                        if (_3 is True) or (_2 == self.MULTIPLE_AXES):
                            _3 = True
                            self.showCombinationMultipleAxes()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.LINE):
                    _1 = True
                    _4 = chartName
                    _5 = False
                    while True:
                        if _4 == self.BASIC:
                            _5 = True
                            self.showLine()
                            break
                        if (_5 is True) or (_4 == self.CLICK_TO_ADD_POINT):
                            _5 = True
                            self.showClickToAddPoint()
                            break
                        if (_5 is True) or (_4 == self.WITH_DATA_LABELS):
                            _5 = True
                            self.showLineWithDataLabels()
                            break
                        if (_5 is True) or (_4 == self.TIMESERIES_ZOOMABLE):
                            _5 = True
                            self.showTimeSeriesZoomable()
                            break
                        if (_5 is True) or (_4 == self.MASTER_DETAIL):
                            _5 = True
                            self.showMasterDetail()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.BAR):
                    _1 = True
                    _6 = chartName
                    _7 = False
                    while True:
                        if _6 == self.BASIC:
                            _7 = True
                            self.showBarBasic()
                            break
                        if (_7 is True) or (_6 == self.STACKED):
                            _7 = True
                            self.showBarStacked()
                            break
                        if (_7 is True) or (_6 == self.WITH_NEGATIVE_STACK):
                            _7 = True
                            self.showBarWithNegStack()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.COLUMN):
                    _1 = True
                    _8 = chartName
                    _9 = False
                    while True:
                        if _8 == self.BASIC:
                            _9 = True
                            self.showColumnBasic()
                            break
                        if (_9 is True) or (_8 == self.WITH_NEGATIVE_VALUES):
                            _9 = True
                            self.showColumnWithNegValues()
                            break
                        if (_9 is True) or (_8 == self.STACKED):
                            _9 = True
                            self.showColumnStacked()
                            break
                        if (_9 is True) or (_8 == self.STACKED_AND_GROUPED):
                            _9 = True
                            self.showColumnStackedAndGrouped()
                            break
                        if (_9 is True) or (_8 == self.STACKED_PERCENT):
                            _9 = True
                            self.showColumnStackedPercent()
                            break
                        if (_9 is True) or (_8 == self.WITH_ROTATED_LABELS):
                            _9 = True
                            self.showColumnWithRotatedLabels()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.AREA):
                    _1 = True
                    _10 = chartName
                    _11 = False
                    while True:
                        if _10 == self.BASIC:
                            _11 = True
                            self.showAreaBasic()
                            break
                        if (_11 is True) or (_10 == self.WITH_NEGATIVE_VALUES):
                            _11 = True
                            self.showAreaWithNegValues()
                            break
                        if (_11 is True) or (_10 == self.STACKED):
                            _11 = True
                            self.showAreaStacked()
                            break
                        if (_11 is True) or (_10 == self.PERCENTAGE):
                            _11 = True
                            self.showAreaPercent()
                            break
                        if (_11 is True) or (_10 == self.INVERTED_AXES):
                            _11 = True
                            self.showAreaInvertedAxes()
                            break
                        if (_11 is True) or (_10 == self.WITH_MISSING_POINTS):
                            _11 = True
                            self.showAreaWithMissingPoints()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.AREASPLINE):
                    _1 = True
                    _12 = chartName
                    _13 = False
                    while True:
                        if _12 == self.BASIC:
                            _13 = True
                            self.showAreaSpline()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.PIE):
                    _1 = True
                    _14 = chartName
                    _15 = False
                    while True:
                        if _14 == self.BASIC:
                            _15 = True
                            self.showPie()
                            break
                        if (_15 is True) or (_14 == self.WITH_LEGEND):
                            _15 = True
                            self.showPieWithLegend()
                            break
                        if (_15 is True) or (_14 == self.DONUT):
                            _15 = True
                            self.showDonut()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.SCATTER):
                    _1 = True
                    _16 = chartName
                    _17 = False
                    while True:
                        if _16 == self.BASIC:
                            _17 = True
                            self.showScatter()
                            break
                        break
                    break
                if (_1 is True) or (_0 == self.SPLINE):
                    _1 = True
                    _18 = chartName
                    _19 = False
                    while True:
                        if _18 == self.BASIC:
                            _19 = True
                            self.showSpline()
                            break
                        if (_19 is True) or (_18 == self.WITH_PLOTBANDS):
                            _19 = True
                            self.showSplineWithPlotBands()
                            break
                        if (_19 is True) or (_18 == self.WITH_SYMBOLS):
                            _19 = True
                            self.showSplineWithSymbol()
                            break
                        if (_19 is True) or (_18 == self.UPDATING_EACH_SECOND):
                            _19 = True
                            self.showSplineUpdatingEachSecond()
                            break
                        break
                    break
                if True:
                    _1 = True
                    self.getApplication().getMainWindow().showNotification('Error occurred during chart processing! Try again!!!')
                break
        else:
            self.getApplication().getMainWindow().showNotification('Error occurred during chart processing! Try again!!!')

    def showMasterDetail(self):
        # Create the master chart
        masterChart = self.getMasterChart()
        # Create detail chart
        detailChart = self.getDetailChart(masterChart)
        # Register events

        class _1_(ChartZoomListener):

            def chartZoom(self, chartZoomEvent):
                # chartZoomEvent.getChartArea().get
                masterChartSeries = self.masterChart.getSeries('USD to EUR')
                min = chartZoomEvent.getChartArea().getxAxisMin()
                max = chartZoomEvent.getChartArea().getxAxisMax()
                detailPoints = LinkedHashSet()
                detailChartSeries = self.detailChart.getSeries('USD to EUR')
                self.detailChart.removeSeries(detailChartSeries)
                for point in masterChartSeries.getPoints():
                    if point.getX().getTime() > min and point.getX().getTime() < max:
                        detailPoints.add(DateTimePoint(detailChartSeries, point.getX(), point.getY()))
                # Update series with new points
                detailChartSeries.setSeriesPoints(detailPoints)
                self.detailChart.addSeries(detailChartSeries)
                self.detailChart.refresh()
                # Update plotbands
                masterDateTimeAxis = self.masterChart.getConfig().getXAxes().next()
                masterDateTimeAxis.removePlotBand('mask-before')
                plotBandBefore = DateTimePlotBand('mask-before')
                plotBandBefore.setRange(DateTimeRange(InvientChartsDemoWin_this._masterChartMinDate, Date(min)))
                plotBandBefore.setColor(RGBA(0, 0, 0, 0.2))
                masterDateTimeAxis.addPlotBand(plotBandBefore)
                masterDateTimeAxis.removePlotBand('mask-after')
                plotBandAfter = DateTimePlotBand('mask-after')
                plotBandAfter.setRange(DateTimeRange(Date(max), InvientChartsDemoWin_this._masterChartMaxDate))
                plotBandAfter.setColor(RGBA(0, 0, 0, 0.2))
                masterDateTimeAxis.addPlotBand(plotBandAfter)
                self.masterChart.refresh()

        _1_ = _1_()
        masterChart.addListener(_1_)
        # Add master
        self.addChart(masterChart, False, False, False, False)
        # Add detail
        self.addChart(detailChart, True, True, False)

    def getDetailChart(self, masterChart):
        detailChartConfig = InvientChartsConfig()
        detailChartConfig.getGeneralChartConfig().setMargin(Margin())
        detailChartConfig.getGeneralChartConfig().getMargin().setBottom(120)
        detailChartConfig.getGeneralChartConfig().getMargin().setLeft(50)
        detailChartConfig.getGeneralChartConfig().getMargin().setRight(20)
        detailChartConfig.getGeneralChartConfig().setReflow(False)
        detailChartConfig.getCredit().setEnabled(False)
        detailChartConfig.getTitle().setText('Historical USD to EUR Exchange Rate')
        detailChartConfig.getSubtitle().setText('Select an area by dragging across the lower chart')
        detailXAxis = DateTimeAxis()
        detailXAxes = LinkedHashSet()
        detailXAxes.add(detailXAxis)
        detailChartConfig.setXAxes(detailXAxes)
        detailYAxis = NumberYAxis()
        detailYAxis.setTitle(AxisTitle(''))
        detailYAxes = LinkedHashSet()
        detailYAxes.add(detailYAxis)
        detailChartConfig.setYAxes(detailYAxes)
        detailChartConfig.getTooltip().setFormatterJsFunc('function() {' + ' var point = this.points[0];' + ' return \'<b>\'+ point.series.name +\'</b><br/>\' + ' + ' $wnd.Highcharts.dateFormat(\'%A %B %e %Y\', this.x) + \':<br/>\' + ' + ' \'1 USD = \'+ $wnd.Highcharts.numberFormat(point.y, 2) +\' EUR\';' + '}')
        detailChartConfig.getTooltip().setShared(True)
        detailChartConfig.getLegend().setEnabled(False)
        lineCfg = LineConfig()
        marker = SymbolMarker(False)
        lineCfg.setMarker(marker)
        marker.setHoverState(MarkerState())
        marker.getHoverState().setEnabled(True)
        marker.getHoverState().setRadius(3)
        detailChartConfig.addSeriesConfig(lineCfg)
        detailChart = InvientCharts(detailChartConfig)
        # Line instance configuration
        lineSeriesCfg = LineConfig()
        lineSeriesCfg.setPointStart(self._detailChartPointStartDate.getTime())
        lineSeriesCfg.setPointInterval(24 * 3600 * 1000.0)
        lineSeriesCfg.setColor(RGB(69, 114, 167))
        detailSeries = DateTimeSeries('USD to EUR', SeriesType.LINE, lineSeriesCfg)
        detailPoints = LinkedHashSet()
        masterChartSeries = masterChart.getSeries('USD to EUR')
        for point in masterChartSeries.getPoints():
            if point.getX().getTime() >= self._detailChartPointStartDate.getTime():
                detailPoints.add(DateTimePoint(detailSeries, point.getY()))
        detailSeries.setSeriesPoints(detailPoints)
        detailChart.addSeries(detailSeries)
        return detailChart

    _masterChartMinDate = getDateZeroTime(2006, 0, 1)
    _masterChartMaxDate = getDateZeroTime(2008, 11, 31)
    _detailChartPointStartDate = getDateZeroTime(2008, 7, 1)

    def getMasterChart(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setReflow(False)
        chartConfig.getGeneralChartConfig().setBorderWidth(0)
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getGeneralChartConfig().getMargin().setLeft(50)
        chartConfig.getGeneralChartConfig().getMargin().setRight(20)
        chartConfig.getGeneralChartConfig().setZoomType(ZoomType.X)
        chartConfig.getGeneralChartConfig().setClientZoom(False)
        chartConfig.getGeneralChartConfig().setHeight(80)
        chartConfig.getTitle().setText('')
        xAxis = DateTimeAxis()
        xAxis.setShowLastLabel(True)
        xAxis.setMaxZoom(14 * 24 * 3600000)
        plotBand = DateTimePlotBand('mask-before')
        plotBand.setRange(DateTimeRange(self._masterChartMinDate, self._detailChartPointStartDate))
        plotBand.setColor(RGBA(0, 0, 0, 0.2))
        xAxis.addPlotBand(plotBand)
        xAxis.setTitle(AxisTitle(''))
        xAxes = LinkedHashSet()
        xAxes.add(xAxis)
        chartConfig.setXAxes(xAxes)
        yAxis = NumberYAxis()
        yAxis.setShowFirstLabel(False)
        yAxis.setMin(0.6)
        yAxis.setGrid(Grid())
        yAxis.getGrid().setLineWidth(0)
        yAxis.setLabel(YAxisDataLabel(False))
        yAxis.setTitle(AxisTitle(''))
        yAxes = LinkedHashSet()
        yAxes.add(yAxis)
        chartConfig.setYAxes(yAxes)
        chartConfig.getTooltip().setFormatterJsFunc('function() { return false; }')
        chartConfig.getLegend().setEnabled(False)
        chartConfig.getCredit().setEnabled(False)
        # Plot options
        areaCfg = AreaConfig()
        colorStops = list()
        colorStops.add(LinearColorStop(0, RGB(69, 114, 167)))
        colorStops.add(LinearColorStop(1, RGBA(0, 0, 0, 0)))
        # Fill color
        areaCfg.setFillColor(Gradient.LinearGradient(0, 0, 0, 70, colorStops))
        areaCfg.setLineWidth(1)
        areaCfg.setMarker(SymbolMarker(False))
        areaCfg.setShadow(False)
        areaCfg.setEnableMouseTracking(False)
        areaCfg.setHoverState(SeriesState())
        areaCfg.getHoverState().setLineWidth(1)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        # Provide methods to set pointInterval and pointStart and delegate call
        # to SeriesConfig
        seriesDataCfg = AreaConfig()
        seriesDataCfg.setPointInterval(24 * 3600 * 1000.0)
        seriesDataCfg.setPointStart(self._masterChartMinDate.getTime())
        masterChartSeries = DateTimeSeries('USD to EUR', SeriesType.AREA, seriesDataCfg)
        masterChartSeries.setSeriesPoints(self.getMasterDetailData(masterChartSeries))
        chart.addSeries(masterChartSeries)
        return chart

    def showLine(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.LINE)
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getGeneralChartConfig().getMargin().setRight(130)
        chartConfig.getGeneralChartConfig().getMargin().setBottom(25)
        chartConfig.getTitle().setX(-20)
        chartConfig.getTitle().setText('Monthly Average Temperature')
        chartConfig.getSubtitle().setText('Source: WorldClimate.com')
        chartConfig.getTitle().setX(-20)
        categoryAxis = CategoryAxis()
        categoryAxis.setCategories(Arrays.asList('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(categoryAxis)
        chartConfig.setXAxes(xAxesSet)
        numberYAxis = NumberYAxis()
        numberYAxis.setTitle(AxisTitle('Temperature (°C)'))
        plotLine = NumberPlotLine('TempAt0')
        plotLine.setValue(NumberValue(0.0))
        plotLine.setWidth(1)
        plotLine.setZIndex(1)
        plotLine.setColor(RGB(128, 128, 128))
        numberYAxis.addPlotLine(plotLine)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(numberYAxis)
        chartConfig.setYAxes(yAxesSet)
        legend = Legend()
        legend.setLayout(Layout.VERTICAL)
        legendPos = Position()
        legendPos.setAlign(HorzAlign.RIGHT)
        legendPos.setVertAlign(VertAlign.TOP)
        legendPos.setX(-10)
        legendPos.setY(100)
        legend.setPosition(legendPos)
        legend.setBorderWidth(0)
        chartConfig.setLegend(legend)
        # Series data label formatter
        lineCfg = LineConfig()
        chartConfig.addSeriesConfig(lineCfg)
        # Tooltip formatter
        chartConfig.getTooltip().setFormatterJsFunc('function() { ' + ' return \'<b>\' + this.series.name + \'</b><br/>\' +  this.x + \': \'+ this.y +\'°C\'' + '}')
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Tokyo')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6))
        chart.addSeries(seriesData)
        seriesData = XYSeries('New York')
        seriesData.setSeriesPoints(self.getPoints(seriesData, -0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Berlin')
        seriesData.setSeriesPoints(self.getPoints(seriesData, -0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0))
        chart.addSeries(seriesData)
        seriesData = XYSeries('London')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showClickToAddPoint(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SCATTER)
        chartConfig.getGeneralChartConfig().setMargin(Margin(70, 50, 60, 80))
        chartConfig.getTitle().setText('User supplied data')
        chartConfig.getSubtitle().setText('Click the plot area to add a point. Click a point to remove it.')
        xAxis = NumberXAxis()
        xAxis.setMinPadding(0.2)
        xAxis.setMaxPadding(0.2)
        xAxis.setMaxZoom(60)
        xAxes = LinkedHashSet()
        xAxes.add(xAxis)
        chartConfig.setXAxes(xAxes)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Value'))
        yAxis.setMinPadding(0.2)
        yAxis.setMaxPadding(0.2)
        yAxis.setMaxZoom(60)
        plotLine = NumberPlotLine('At0')
        plotLine.setValue(NumberValue(0.0))
        plotLine.setWidth(1)
        plotLine.setColor(RGB(128, 128, 128))
        yAxis.addPlotLine(plotLine)
        yAxes = LinkedHashSet()
        yAxes.add(yAxis)
        chartConfig.setYAxes(yAxes)
        chartConfig.getLegend().setEnabled(False)
        scatterCfg = ScatterConfig()
        scatterCfg.setLineWidth(1)
        chartConfig.addSeriesConfig(scatterCfg)
        # chart data
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('User Supplied Data')
        seriesData.addPoint(DecimalPoint(seriesData, 20, 20))
        seriesData.addPoint(DecimalPoint(seriesData, 80, 80))
        chart.addSeries(seriesData)

        class _2_(ChartClickListener):

            def chartClick(self, chartClickEvent):
                InvientChartsDemoWin_this.logEventInfo('chartClick', chartClickEvent.getPoint().getX(), chartClickEvent.getPoint().getY(), chartClickEvent.getMousePosition().getMouseX(), chartClickEvent.getMousePosition().getMouseY())
                xySeries = chartClickEvent.getChart().getSeries('User Supplied Data')
                xySeries.addPoint(DecimalPoint(xySeries, chartClickEvent.getPoint().getX(), chartClickEvent.getPoint().getY()))

        _2_ = _2_()
        chart.addListener(_2_)

        class _3_(PointClickListener):

            def pointClick(self, pointClickEvent):
                InvientChartsDemoWin_this.logEventInfo('pointClick', pointClickEvent.getPoint().getSeries().getName(), pointClickEvent.getCategory(), pointClickEvent.getPoint().getX(), pointClickEvent.getPoint().getY(), pointClickEvent.getMousePosition().getMouseX(), pointClickEvent.getMousePosition().getMouseY())
                xySeries = pointClickEvent.getChart().getSeries('User Supplied Data')
                if len(xySeries.getPoints()) > 1:
                    # remove the clicked point
                    xySeries.removePoint(pointClickEvent.getPoint())

        _3_ = _3_()
        chart.addListener(_3_)
        self.addChart(chart, False, False)

    def showLineWithDataLabels(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getTitle().setText('Monthly Average Temperature')
        chartConfig.getSubtitle().setText('Source: WorldClimate.com')
        categoryAxis = CategoryAxis()
        categoryAxis.setCategories(Arrays.asList('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(categoryAxis)
        chartConfig.setXAxes(xAxesSet)
        numberYAxis = NumberYAxis()
        numberYAxis.setTitle(AxisTitle('Temperature (°C)'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(numberYAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setEnabled(False)
        # Series data label formatter
        lineCfg = LineConfig()
        lineCfg.setDataLabel(DataLabel())
        lineCfg.getDataLabel().setEnabled(True)
        lineCfg.setEnableMouseTracking(False)
        chartConfig.addSeriesConfig(lineCfg)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Tokyo')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6))
        chart.addSeries(seriesData)
        seriesData = XYSeries('London')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showBarStacked(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.BAR)
        chartConfig.getTitle().setText('Stacked bar chart')
        xAxis = CategoryAxis()
        categories = Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas')
        xAxis.setCategories(categories)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        numberYAxis = NumberYAxis()
        numberYAxis.setMin(0.0)
        numberYAxis.setTitle(AxisTitle('Total fruit consumption'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(numberYAxis)
        chartConfig.setYAxes(yAxesSet)
        legend = Legend()
        legend.setBackgroundColor(RGB(255, 255, 255))
        legend.setReversed(True)
        chartConfig.setLegend(legend)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\'+ this.series.name +\': \'+ this.y +\'\'; ' + '}')
        seriesCfg = SeriesConfig()
        seriesCfg.setStacking(Stacking.NORMAL)
        chartConfig.addSeriesConfig(seriesCfg)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('John')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 5, 3, 4, 7, 2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Jane')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, 2, 3, 2, 1))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 4, 4, 2, 5))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showBarBasic(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.BAR)
        chartConfig.getTitle().setText('Historic World Population by Region')
        chartConfig.getSubtitle().setText('Source: Wikipedia.org')
        xAxisMain = CategoryAxis()
        categories = Arrays.asList('Africa', 'America', 'Asia', 'Europe', 'Oceania')
        xAxisMain.setCategories(categories)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxisMain)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Population (millions)'))
        yAxis.getTitle().setAlign(AxisTitleAlign.HIGH)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.series.name +\': \'+ this.y +\' millions\';' + '}')
        barCfg = BarConfig()
        barCfg.setDataLabel(DataLabel())
        chartConfig.addSeriesConfig(barCfg)
        legend = Legend()
        legend.setLayout(Layout.VERTICAL)
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.RIGHT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(-100)
        legend.getPosition().setY(100)
        legend.setFloating(True)
        legend.setBorderWidth(1)
        legend.setBackgroundColor(RGB(255, 255, 255))
        legend.setShadow(True)
        chartConfig.setLegend(legend)
        chartConfig.getCredit().setEnabled(False)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Year 1800')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 107, 31, 635, 203, 2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Year 1900')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 133, 156, 947, 408, 6))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Year 2008')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 973, 914, 4054, 732, 34))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showBarWithNegStack(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.BAR)
        chartConfig.getTitle().setText('Population pyramid for Germany, midyear 2010')
        chartConfig.getSubtitle().setText('Source: www.census.gov')
        xAxisMain = CategoryAxis()
        categories = Arrays.asList('0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100 +')
        xAxisMain.setCategories(categories)
        xAxisMain.setReversed(False)
        xAxesSet = LinkedHashSet()
        # Opposite axis
        xAxesSet.add(xAxisMain)
        xAxis = CategoryAxis()
        xAxis.setCategories(categories)
        xAxis.setOpposite(True)
        xAxis.setReversed(False)
        xAxis.setLinkedTo(xAxisMain)
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle(''))
        yAxis.setMin(-4000000.0)
        yAxis.setMax(4000000.0)
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return (Math.abs(this.value) / 1000000) + \'M\';' + ' }')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        tooltip = Tooltip()
        tooltip.setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.series.name +\', age \'+ this.point.category +\'</b><br/>\' + ' + ' \'Population: \'+ Highcharts.numberFormat(Math.abs(this.point.y), 0); ' + '}')
        series = SeriesConfig()
        series.setStacking(Stacking.NORMAL)
        chartConfig.addSeriesConfig(series)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Male')
        seriesData.setSeriesPoints(self.getPoints(seriesData, -1746181, -1884428, -2089758, -2222362, -2537431, -2507081, -2443179, -2664537, -3556505, -3680231, -3143062, -2721122, -2229181, -2227768, -2176300, -1329968, -836804, -354784, -90569, -28367, -3878))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Female')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 1656154, 1787564, 1981671, 2108575, 2403438, 2366003, 2301402, 2519874, 3360596, 3493473, 3050775, 2759560, 2304444, 2426504, 2568938, 1785638, 1447162, 1005011, 330870, 130632, 21208))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnBasic(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getTitle().setText('Monthly Average Rainfall')
        chartConfig.getSubtitle().setText('Source: WorldClimate.com')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Rainfall (mm)'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        legend = Legend()
        legend.setFloating(True)
        legend.setLayout(Layout.VERTICAL)
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.LEFT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(100)
        legend.getPosition().setY(70)
        legend.setShadow(True)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.x +\': \'+ this.y +\' mm\'; ' + '}')
        colCfg = ColumnConfig()
        colCfg.setPointPadding(0.2)
        colCfg.setBorderWidth(0)
        chartConfig.addSeriesConfig(colCfg)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Tokyo')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4))
        chart.addSeries(seriesData)
        seriesData = XYSeries('New York')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3))
        chart.addSeries(seriesData)
        seriesData = XYSeries('London')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Berlin')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnWithNegValues(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getTitle().setText('Column chart with negative values')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        tooltip = Tooltip()
        tooltip.setFormatterJsFunc('function() {' + ' return \'\' + this.series.name +\': \'+ this.y +\'\'; ' + '}')
        chartConfig.setTooltip(tooltip)
        chartConfig.getCredit().setEnabled(False)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('John')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 5, 3, 4, 7, 2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Jane')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, -2, -3, 2, 1))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 4, 4, -2, 5))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnStacked(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getTitle().setText('Stacked column chart')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Total fruit consumption'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        legend = Legend()
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.RIGHT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(-100)
        legend.getPosition().setY(20)
        legend.setFloating(True)
        legend.setBackgroundColor(RGB(255, 255, 255))
        legend.setBorderWidth(1)
        legend.setShadow(True)
        chartConfig.setLegend(legend)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.x +\'</b><br/>\'+ this.series.name +\': \'+ this.y +\'<br/>\'+' + '        \'Total: \'+ this.point.stackTotal; ' + '}')
        colCfg = ColumnConfig()
        colCfg.setStacking(Stacking.NORMAL)
        chartConfig.addSeriesConfig(colCfg)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('John')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 5, 3, 4, 7, 2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Jane')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, 2, 3, 2, 1))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 4, 4, 2, 5))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnStackedAndGrouped(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getTitle().setText('Total fruit consumtion, grouped by gender')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setAllowDecimals(False)
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Number of fruits'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        series = ColumnConfig()
        series.setStacking(Stacking.NORMAL)
        chartConfig.addSeriesConfig(series)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.x +\'</b><br/>\'+ this.series.name +\': \'+ this.y +\'<br/>\'+ \'Total: \'+ this.point.stackTotal;' + '}')
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('John')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 5, 3, 4, 7, 2))
        seriesData.setStack('male')
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 4, 4, 2, 5))
        seriesData.setStack('male')
        chart.addSeries(seriesData)
        seriesData = XYSeries('Jane')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, 5, 6, 2, 1))
        seriesData.setStack('female')
        chart.addSeries(seriesData)
        seriesData = XYSeries('Janet')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 0, 4, 4, 3))
        seriesData.setStack('female')
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnStackedPercent(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getTitle().setText('Stacked column chart')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Total fruit consumption'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        series = ColumnConfig()
        series.setStacking(Stacking.PERCENT)
        chartConfig.addSeriesConfig(series)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.series.name +\': \'+ this.y +\' (\'+ Math.round(this.percentage) +\'%)\'; ' + '}')
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('John')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 5, 3, 4, 7, 2))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 4, 4, 2, 5))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Jane')
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, 2, 3, 2, 1))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showColumnWithRotatedLabels(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.COLUMN)
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getGeneralChartConfig().getMargin().setTop(50)
        chartConfig.getGeneralChartConfig().getMargin().setRight(50)
        chartConfig.getGeneralChartConfig().getMargin().setBottom(100)
        chartConfig.getGeneralChartConfig().getMargin().setLeft(80)
        chartConfig.getTitle().setText('World\\'s largest cities per 2008')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Tokyo', 'Jakarta', 'New York', 'Seoul', 'Manila', 'Mumbai', 'Sao Paulo', 'Mexico City', 'Dehli', 'Osaka', 'Cairo', 'Kolkata', 'Los Angeles', 'Shanghai', 'Moscow', 'Beijing', 'Buenos Aires', 'Guangzhou', 'Shenzhen', 'Istanbul'))
        xAxis.setLabel(XAxisDataLabel())
        xAxis.getLabel().setRotation(-45)
        xAxis.getLabel().setAlign(HorzAlign.RIGHT)
        xAxis.getLabel().setStyle('{ font: \'normal 13px Verdana, sans-serif\' }')
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxis.setTitle(AxisTitle('Population (millions)'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.setLegend(Legend(False))
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.x +\'</b><br/>\'+ \'Population in 2008: \'+ $wnd.Highcharts.numberFormat(this.y, 1) + ' + ' \' millions\' ' + '}')
        chart = InvientCharts(chartConfig)
        colCfg = ColumnConfig()
        colCfg.setDataLabel(DataLabel())
        colCfg.getDataLabel().setRotation(-90)
        colCfg.getDataLabel().setAlign(HorzAlign.RIGHT)
        colCfg.getDataLabel().setX(-3)
        colCfg.getDataLabel().setY(10)
        colCfg.getDataLabel().setColor(RGB(255, 255, 255))
        colCfg.getDataLabel().setFormatterJsFunc('function() {' + ' return this.y; ' + '}')
        colCfg.getDataLabel().setStyle(' { font: \'normal 13px Verdana, sans-serif\' } ')
        seriesData = XYSeries('Population', colCfg)
        seriesData.setSeriesPoints(self.getPoints(seriesData, 34.4, 21.8, 20.1, 20, 19.6, 19.5, 19.1, 18.4, 18, 17.3, 16.8, 15, 14.7, 14.5, 13.3, 12.8, 12.4, 11.8, 11.7, 11.2))
        chart.addSeries(seriesData)
        self.addChart(chart)

    def showAreaWithNegValues(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getTitle().setText('Area chart with negative values')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        chartConfig.getCredit().setEnabled(False)
        chart = InvientCharts(chartConfig)
        series = XYSeries('John')
        series.setSeriesPoints(self.getPoints(series, 5, 3, 4, 7, 2))
        chart.addSeries(series)
        series = XYSeries('Jane')
        series.setSeriesPoints(self.getPoints(series, 2, -2, -3, 2, 1))
        chart.addSeries(series)
        series = XYSeries('Joe')
        series.setSeriesPoints(self.getPoints(series, 3, 4, 4, -2, 5))
        chart.addSeries(series)
        self.addChart(chart)

    def showAreaInvertedAxes(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getGeneralChartConfig().setInverted(True)
        chartConfig.getTitle().setText('Average fruit consumption during one week')
        chartConfig.getSubtitle().setStyle('{ position: \'absolute\', right: \'0px\', bottom: \'10px\'}')
        legend = Legend()
        legend.setFloating(True)
        legend.setLayout(Layout.VERTICAL)
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.RIGHT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(-150)
        legend.getPosition().setY(100)
        legend.setBorderWidth(1)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Number of units'))
        yAxis.setMin(0.0)
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value; ' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.x + \': \' + this.y; ' + '}')
        areaCfg = AreaConfig()
        areaCfg.setFillOpacity(0.5)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('John')
        series.setSeriesPoints(self.getPoints(series, 3, 4, 3, 5, 4, 10, 12))
        chart.addSeries(series)
        series = XYSeries('Jane')
        series.setSeriesPoints(self.getPoints(series, 1, 3, 4, 3, 3, 5, 4))
        chart.addSeries(series)
        self.addChart(chart)

    def showAreaWithMissingPoints(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getGeneralChartConfig().setSpacing(Spacing())
        chartConfig.getGeneralChartConfig().getSpacing().setBottom(30)
        chartConfig.getTitle().setText('Fruit consumption *')
        chartConfig.getSubtitle().setText('* Jane\\'s banana consumption is unknown')
        chartConfig.getSubtitle().setFloating(True)
        chartConfig.getSubtitle().setAlign(HorzAlign.RIGHT)
        chartConfig.getSubtitle().setVertAlign(VertAlign.BOTTOM)
        chartConfig.getSubtitle().setY(15)
        legend = Legend()
        legend.setFloating(True)
        legend.setLayout(Layout.VERTICAL)
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.LEFT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(150)
        legend.getPosition().setY(100)
        legend.setBorderWidth(1)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Pears', 'Oranges', 'Bananas', 'Grapes', 'Plums', 'Strawberries', 'Raspberries'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Y-Axis'))
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value; ' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.series.name +\'</b><br/>\'+ this.x +\': \'+ this.y;' + '}')
        chartConfig.getCredit().setEnabled(False)
        areaCfg = AreaConfig()
        areaCfg.setFillOpacity(0.5)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('John')
        series.setSeriesPoints(self.getPoints(series, 0, 1, 4, 4, 5, 2, 3, 7))
        chart.addSeries(series)
        series = XYSeries('Jane')
        series.addPoint(DecimalPoint(series, 1.0), DecimalPoint(series, 0.0), DecimalPoint(series, 3.0), DecimalPoint(series), DecimalPoint(series, 3.0), DecimalPoint(series, 1.0), DecimalPoint(series, 2.0), DecimalPoint(series, 1.0))
        chart.addSeries(series)
        self.addChart(chart)

    def showAreaStacked(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getTitle().setText('Historic and Estimated Worldwide Population Growth by Region')
        chartConfig.getSubtitle().setText('Source: Wikipedia.org')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('1750', '1800', '1850', '1900', '1950', '1999', '2050'))
        tick = Tick()
        tick.setPlacement(TickmarkPlacement.ON)
        xAxis.setTick(tick)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Billions'))
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value / 1000; ' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\'+ this.x +\': \'+ $wnd.Highcharts.numberFormat(this.y, 0, \',\') +\' millions\';' + '}')
        areaCfg = AreaConfig()
        areaCfg.setStacking(Stacking.NORMAL)
        areaCfg.setLineColor(RGB(102, 102, 102))
        areaCfg.setLineWidth(1)
        marker = SymbolMarker()
        marker.setLineColor(RGB(102, 102, 102))
        marker.setLineWidth(1)
        areaCfg.setMarker(marker)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('Asia')
        series.setSeriesPoints(self.getPoints(series, 502, 635, 809, 947, 1402, 3634, 5268))
        chart.addSeries(series)
        series = XYSeries('Africa')
        series.setSeriesPoints(self.getPoints(series, 106, 107, 111, 133, 221, 767, 1766))
        chart.addSeries(series)
        series = XYSeries('Europe')
        series.setSeriesPoints(self.getPoints(series, 163, 203, 276, 408, 547, 729, 628))
        chart.addSeries(series)
        series = XYSeries('America')
        series.setSeriesPoints(self.getPoints(series, 18, 31, 54, 156, 339, 818, 1201))
        chart.addSeries(series)
        series = XYSeries('Oceania')
        series.setSeriesPoints(self.getPoints(series, 2, 2, 2, 6, 13, 30, 46))
        chart.addSeries(series)
        self.addChart(chart)

    def showAreaPercent(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getTitle().setText('Historic and Estimated Worldwide Population Distribution by Region')
        chartConfig.getSubtitle().setText('Source: Wikipedia.org')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('1750', '1800', '1850', '1900', '1950', '1999', '2050'))
        tick = Tick()
        tick.setPlacement(TickmarkPlacement.ON)
        xAxis.setTick(tick)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Percent'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.x +\': \' + $wnd.Highcharts.numberFormat(this.percentage, 1) + ' + '    \'% (\'+ $wnd.Highcharts.numberFormat(this.y, 0, \',\') +\' millions)\'; ' + '}')
        areaCfg = AreaConfig()
        areaCfg.setStacking(Stacking.PERCENT)
        areaCfg.setLineColor(RGB(255, 255, 255))
        areaCfg.setLineWidth(1)
        marker = SymbolMarker()
        marker.setLineColor(RGB(255, 255, 255))
        marker.setLineWidth(1)
        areaCfg.setMarker(marker)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('Asia')
        series.setSeriesPoints(self.getPoints(series, 502, 635, 809, 947, 1402, 3634, 5268))
        chart.addSeries(series)
        series = XYSeries('Africa')
        series.setSeriesPoints(self.getPoints(series, 106, 107, 111, 133, 221, 767, 1766))
        chart.addSeries(series)
        series = XYSeries('Europe')
        series.setSeriesPoints(self.getPoints(series, 163, 203, 276, 408, 547, 729, 628))
        chart.addSeries(series)
        series = XYSeries('America')
        series.setSeriesPoints(self.getPoints(series, 18, 31, 54, 156, 339, 818, 1201))
        chart.addSeries(series)
        series = XYSeries('Oceania')
        series.setSeriesPoints(self.getPoints(series, 2, 2, 2, 6, 13, 30, 46))
        chart.addSeries(series)
        self.addChart(chart)

    def showAreaBasic(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREA)
        chartConfig.getTitle().setText('US and USSR nuclear stockpiles')
        chartConfig.getSubtitle().setText('Source: <a href=\'http://thebulletin.metapress.com/content/c4120650912x74k7/fulltext.pdf\'>thebulletin.metapress.com</a>')
        xAxis = NumberXAxis()
        xAxis.setLabel(XAxisDataLabel())
        xAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value;' + '}')
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Nuclear weapon states'))
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value / 1000 +\'k\';' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return this.series.name +\' produced <b>\'+' + '    $wnd.Highcharts.numberFormat(this.y, 0) +\'</b><br/>warheads in \'+ this.x;' + '}')
        areaCfg = AreaConfig()
        areaCfg.setPointStart(1940.0)
        marker = SymbolMarker()
        areaCfg.setMarker(marker)
        marker.setEnabled(False)
        marker.setSymbol(Symbol.CIRCLE)
        marker.setRadius(2)
        marker.setHoverState(MarkerState(True))
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        # Series -
        usaAreaCfg = AreaConfig()
        usaAreaCfg.setPointStart(1940.0)
        series = XYSeries('USA', usaAreaCfg)
        points = LinkedHashSet()
        self.addNullPoints(points, series, 5)
        points.addAll(self.getPoints(series, 6, 11, 32, 110, 235, 369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605, 24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        # Series -
        russiaAreaCfg = AreaConfig()
        russiaAreaCfg.setPointStart(1940.0)
        series = XYSeries('USSR/Russia', russiaAreaCfg)
        points = LinkedHashSet()
        self.addNullPoints(points, series, 10)
        points.addAll(self.getPoints(series, 5, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322, 4238, 5221, 6129, 7089, 8339, 9399, 10538, 11643, 13092, 14478, 15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049, 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000, 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000, 21000, 20000, 19000, 18000, 18000, 17000, 16000))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        self.addChart(chart)

    def addNullPoints(self, points, series, howManyNullPoints):
        _0 = True
        cnt = 0
        while True:
            if _0 is True:
                _0 = False
            else:
                cnt += 1
            if not (cnt < howManyNullPoints):
                break
            points.add(DecimalPoint(series))

    def showAreaSpline(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.AREASPLINE)
        chartConfig.getTitle().setText('Average fruit consumption during one week')
        legend = Legend()
        legend.setLayout(Layout.VERTICAL)
        legendPos = Position()
        legendPos.setAlign(HorzAlign.LEFT)
        legendPos.setVertAlign(VertAlign.TOP)
        legendPos.setX(150)
        legendPos.setY(100)
        legend.setPosition(legendPos)
        legend.setFloating(True)
        legend.setBorderWidth(1)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
        plotBand = NumberPlotBand('sat-sun')
        plotBand.setRange(NumberRange(4.6, 6.5))
        plotBand.setColor(RGBA(68, 170, 213, 0.2))
        xAxis.addPlotBand(plotBand)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Fruit units'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getCredit().setEnabled(False)
        areaSpline = AreaSplineConfig()
        areaSpline.setFillOpacity(0.5)
        chartConfig.addSeriesConfig(areaSpline)
        chart = InvientCharts(chartConfig)
        series = XYSeries('John')
        series.setSeriesPoints(self.getPoints(series, 3, 4, 3, 5, 4, 10, 12))
        chart.addSeries(series)
        series = XYSeries('Jane')
        series.setSeriesPoints(self.getPoints(series, 1, 3, 4, 3, 3, 5, 4))
        chart.addSeries(series)
        self.addChart(chart)

    def showPieWithLegend(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.PIE)
        chartConfig.getTitle().setText('Browser market shares at a specific website, 2010')
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.point.name +\'</b>: \'+ this.y +\' %\'; ' + '}')
        pie = PieConfig()
        pie.setAllowPointSelect(True)
        pie.setCursor('pointer')
        pie.setDataLabel(PieDataLabel(False))
        pie.setShowInLegend(True)
        chartConfig.addSeriesConfig(pie)
        chart = InvientCharts(chartConfig)
        series = XYSeries('Browser Share')
        points = LinkedHashSet()
        points.add(DecimalPoint(series, 'Firefox', 45.0))
        points.add(DecimalPoint(series, 'IE', 26.8))
        config = PointConfig(True)
        points.add(DecimalPoint(series, 'Chrome', 12.8, config))
        points.add(DecimalPoint(series, 'Safari', 8.5))
        points.add(DecimalPoint(series, 'Opera', 6.2))
        points.add(DecimalPoint(series, 'Others', 0.7))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        self.addChart(chart)

    def showDonut(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.PIE)
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getGeneralChartConfig().getMargin().setTop(50)
        chartConfig.getGeneralChartConfig().getMargin().setRight(0)
        chartConfig.getGeneralChartConfig().getMargin().setBottom(0)
        chartConfig.getGeneralChartConfig().getMargin().setLeft(0)
        chartConfig.getTitle().setText('Browser market shares at a specific website')
        chartConfig.getSubtitle().setText('Inner circle: 2008, outer circle: 2010')
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.series.name +\'</b><br/>\'+ ' + '     this.point.name +\': \'+ this.y +\' %\'; ' + '}')
        chart = InvientCharts(chartConfig)
        # Series 1
        pieCfg = PieConfig()
        pieCfg.setInnerSize(65)
        pieCfg.setDataLabel(PieDataLabel(False))
        series = XYSeries('2008', SeriesType.PIE, pieCfg)
        points = LinkedHashSet()
        points.add(self.getPointWithColor(series, 'Firefox', 44.2, RGB(69, 114, 167)))
        points.add(self.getPointWithColor(series, 'IE', 46.6, RGB(170, 70, 67)))
        points.add(self.getPointWithColor(series, 'Chrome', 3.1, RGB(137, 165, 78)))
        points.add(self.getPointWithColor(series, 'Safari', 2.7, RGB(128, 105, 155)))
        points.add(self.getPointWithColor(series, 'Opera', 2.3, RGB(128, 105, 155)))
        points.add(self.getPointWithColor(series, 'Mozilla', 0.4, RGB(219, 132, 61)))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        # Series 1
        pieCfg = PieConfig()
        pieCfg.setInnerSize(150)
        pieCfg.setDataLabel(PieDataLabel())
        pieCfg.setColor(RGB(0, 0, 0))
        pieCfg.getDataLabel().setConnectorColor(RGB(0, 0, 0))
        series = XYSeries('2010', SeriesType.PIE, pieCfg)
        points = LinkedHashSet()
        points.add(self.getPointWithColor(series, 'Firefox', 45.0, RGB(69, 114, 167)))
        points.add(self.getPointWithColor(series, 'IE', 26.8, RGB(170, 70, 67)))
        points.add(self.getPointWithColor(series, 'Chrome', 12.8, RGB(137, 165, 78)))
        points.add(self.getPointWithColor(series, 'Safari', 8.5, RGB(128, 105, 155)))
        points.add(self.getPointWithColor(series, 'Opera', 6.2, RGB(128, 105, 155)))
        points.add(self.getPointWithColor(series, 'Mozilla', 0.2, RGB(219, 132, 61)))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        self.addChart(chart)

    def getPointWithColor(self, series, name, y, color):
        point = DecimalPoint(series, name, y)
        point.setConfig(PointConfig(color))
        return point

    def showPie(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.PIE)
        chartConfig.getTitle().setText('Browser market shares at a specific website, 2010')
        pieCfg = PieConfig()
        pieCfg.setAllowPointSelect(True)
        pieCfg.setCursor('pointer')
        pieCfg.setDataLabel(PieDataLabel())
        pieCfg.getDataLabel().setEnabled(True)
        pieCfg.getDataLabel().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.point.name +\'</b>: \'+ this.y +\' %\';' + '}')
        pieCfg.getDataLabel().setConnectorColor(RGB(0, 0, 0))
        chartConfig.addSeriesConfig(pieCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('Browser Share')
        points = LinkedHashSet()
        points.add(DecimalPoint(series, 'Firefox', 45.0))
        points.add(DecimalPoint(series, 'IE', 26.8))
        config = PointConfig(True)
        points.add(DecimalPoint(series, 'Chrome', 12.8, config))
        points.add(DecimalPoint(series, 'Safari', 8.5))
        points.add(DecimalPoint(series, 'Opera', 6.2))
        points.add(DecimalPoint(series, 'Others', 0.7))
        series.setSeriesPoints(points)
        chart.addSeries(series)
        self.addChart(chart)

    def showScatter(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SCATTER)
        chartConfig.getGeneralChartConfig().setZoomType(ZoomType.XY)
        chartConfig.getTitle().setText('Height Versus Weight of Individuals by Gender')
        chartConfig.getSubtitle().setText('Source: Heinz  2003')
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + this.x + \' cm, \' + this.y + \' kg\'; ' + '}')
        xAxis = NumberXAxis()
        xAxis.setTitle(AxisTitle('Height (cm)'))
        xAxis.setStartOnTick(True)
        xAxis.setEndOnTick(True)
        xAxis.setShowLastLabel(True)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Weight (kg)'))
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        legend = Legend()
        legend.setLayout(Layout.VERTICAL)
        legendPos = Position()
        legendPos.setAlign(HorzAlign.LEFT)
        legendPos.setVertAlign(VertAlign.TOP)
        legendPos.setX(100)
        legendPos.setY(70)
        legend.setPosition(legendPos)
        legend.setFloating(True)
        legend.setBorderWidth(1)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        scatterCfg = ScatterConfig()
        marker = SymbolMarker(5)
        scatterCfg.setMarker(marker)
        marker.setHoverState(MarkerState())
        marker.getHoverState().setEnabled(True)
        marker.getHoverState().setLineColor(RGB(100, 100, 100))
        chartConfig.addSeriesConfig(scatterCfg)
        chart = InvientCharts(chartConfig)
        femaleScatterCfg = ScatterConfig()
        femaleScatterCfg.setColor(RGBA(223, 83, 83, 0.5))
        series = XYSeries('Female', femaleScatterCfg)
        series.setSeriesPoints(self.getScatterFemalePoints(series))
        chart.addSeries(series)
        maleScatterCfg = ScatterConfig()
        maleScatterCfg.setColor(RGBA(119, 152, 191, 0.5))
        series = XYSeries('Male', maleScatterCfg)
        series.setSeriesPoints(self.getScatterMalePoints(series))
        chart.addSeries(series)
        self.addChart(chart)

    def showCombinationScatterWithRegressionLine(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getTitle().setText('Scatter plot with regression line')
        xAxis = NumberXAxis()
        xAxis.setMin(-0.5)
        xAxis.setMax(5.5)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setMin(0.0)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chart = InvientCharts(chartConfig)
        # Line series
        lineCfg = LineConfig()
        lineCfg.setMarker(SymbolMarker(False))
        lineCfg.setHoverState(SeriesState())
        lineCfg.getHoverState().setLineWidth(0)
        lineSeries = XYSeries('Regression Line', lineCfg)
        lineSeries.setType(SeriesType.LINE)
        lineSeries.setSeriesPoints(self.getPoints(lineSeries, [0, 1.11], [5, 4.51]))
        chart.addSeries(lineSeries)
        # Scatter series
        scatterCfg = ScatterConfig()
        scatterCfg.setMarker(SymbolMarker(4))
        scatterSeries = XYSeries('Observations', scatterCfg)
        scatterSeries.setType(SeriesType.SCATTER)
        scatterSeries.setSeriesPoints(self.getPoints(scatterSeries, 1, 1.5, 2.8, 3.5, 3.9, 4.2))
        chart.addSeries(scatterSeries)
        self.addChart(chart)

    def showSpline(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SPLINE)
        chartConfig.getGeneralChartConfig().setInverted(True)
        chartConfig.getGeneralChartConfig().setWidth(500)
        chartConfig.getTitle().setText('Atmosphere Temperature by Altitude')
        chartConfig.getSubtitle().setText('According to the Standard Atmosphere Model')
        xAxis = NumberXAxis()
        xAxis.setReversed(False)
        xAxis.setTitle(AxisTitle('Altitude'))
        xAxis.setLabel(XAxisDataLabel())
        xAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value +\'km\';' + '}')
        xAxis.setMaxPadding(0.05)
        xAxis.setShowLastLabel(True)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Temperature'))
        yAxis.setLineWidth(2)
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value + \'°C\';' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        tooltip = Tooltip()
        tooltip.setFormatterJsFunc('function() {' + ' return \'\' + this.x +\' km: \'+ this.y +\'°C\';' + '}')
        chartConfig.setTooltip(tooltip)
        legend = Legend()
        legend.setEnabled(False)
        chartConfig.setLegend(legend)
        splineCfg = SplineConfig()
        splineCfg.setMarker(SymbolMarker(True))
        chartConfig.addSeriesConfig(splineCfg)
        chart = InvientCharts(chartConfig)
        series = XYSeries('Temperature')
        series.setSeriesPoints(self.getPoints(series, [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1], [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]))
        chart.addSeries(series)
        self.addChart(chart)

    def showSplineWithSymbol(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SPLINE)
        chartConfig.getTitle().setText('Monthly Average Temperature')
        chartConfig.getSubtitle().setText('Source: WorldClimate.com')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Temperature'))
        yAxis.setLabel(YAxisDataLabel())
        yAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value + \'°\';' + '}')
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        tooltip = Tooltip()
        tooltip.setCrosshairs(True)
        tooltip.setShared(True)
        chartConfig.setTooltip(tooltip)
        splineCfg = SplineConfig()
        symbolMarker = SymbolMarker(True)
        symbolMarker.setRadius(4)
        symbolMarker.setLineColor(RGB(102, 102, 102))
        symbolMarker.setLineWidth(1)
        splineCfg.setMarker(symbolMarker)
        chartConfig.addSeriesConfig(splineCfg)
        chart = InvientCharts(chartConfig)
        # Series
        splineCfg = SplineConfig()
        splineCfg.setMarker(SymbolMarker(Symbol.SQUARE))
        series = XYSeries('Tokyo', splineCfg)
        series.setSeriesPoints(self.getPoints(series, 7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2))
        config = PointConfig(ImageMarker('/graphics/sun.png'))
        highest = DecimalPoint(series, 26.5, config)
        series.addPoint(highest)
        series.addPoint(DecimalPoint(series, 23.3))
        series.addPoint(DecimalPoint(series, 18.3))
        series.addPoint(DecimalPoint(series, 13.9))
        series.addPoint(DecimalPoint(series, 9.6))
        chart.addSeries(series)
        # Series
        splineCfg = SplineConfig()
        splineCfg.setMarker(SymbolMarker(Symbol.DIAMOND))
        series = XYSeries('London', splineCfg)
        config = PointConfig(ImageMarker('/graphics/snow.png'))
        lowest = DecimalPoint(series, 3.9, config)
        series.addPoint(lowest)
        series.addPoint(DecimalPoint(series, 4.2))
        series.addPoint(DecimalPoint(series, 5.7))
        series.addPoint(DecimalPoint(series, 8.5))
        series.addPoint(DecimalPoint(series, 11.9))
        series.addPoint(DecimalPoint(series, 15.2))
        series.addPoint(DecimalPoint(series, 17.0))
        series.addPoint(DecimalPoint(series, 16.6))
        series.addPoint(DecimalPoint(series, 14.2))
        series.addPoint(DecimalPoint(series, 10.3))
        series.addPoint(DecimalPoint(series, 6.6))
        series.addPoint(DecimalPoint(series, 4.8))
        chart.addSeries(series)
        self.addChart(chart)

    def showSplineUpdatingEachSecond(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SPLINE)
        chartConfig.getGeneralChartConfig().setMargin(Margin())
        chartConfig.getGeneralChartConfig().getMargin().setRight(10)
        chartConfig.getTitle().setText('Live random data')
        xAxis = DateTimeAxis()
        xAxis.setTick(Tick())
        xAxis.getTick().setPixelInterval(150)
        xAxes = LinkedHashSet()
        xAxes.add(xAxis)
        chartConfig.setXAxes(xAxes)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Value'))
        yAxis.addPlotLine(plotLine = NumberPlotLine('LineAt0'))
        plotLine.setValue(NumberValue(0.0))
        plotLine.setWidth(1)
        plotLine.setColor(RGB(128, 128, 128))
        yAxes = LinkedHashSet()
        yAxes.add(yAxis)
        chartConfig.setYAxes(yAxes)
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'<b>\'+ this.series.name +\'</b><br/>\'+ ' + ' $wnd.Highcharts.dateFormat(\'%Y-%m-%d %H:%M:%S\', this.x) +\'<br/>\'+ ' + ' $wnd.Highcharts.numberFormat(this.y, 2);' + '}')
        chartConfig.getLegend().setEnabled(False)
        chart = InvientCharts(chartConfig)
        seriesData = DateTimeSeries('Random Data', True)
        points = LinkedHashSet()
        dtNow = Date()
        # Add random data.
        _0 = True
        cnt = -19
        while True:
            if _0 is True:
                _0 = False
            else:
                cnt += 1
            if not (cnt <= 0):
                break
            points.add(DateTimePoint(seriesData, self.getUpdatedDate(dtNow, cnt * 1000), self.Math.random()))
        seriesData.setSeriesPoints(points)
        chart.addSeries(seriesData)
        self.addChart(chart, False, False, False)
        self._indicator = ProgressIndicator(0.2)
        self._indicator.setPollingInterval(1000)
        self._indicator.setStyleName('i-progressindicator-invisible')
        self._rightLayout.addComponent(self._indicator)
        if not self.isAppRunningOnGAE():
            self._splineThread = self.SelfUpdateSplineThread(chart)
            self._splineThread.start()
        else:
            self.getApplication().getMainWindow().showNotification('This chart does not auto-update because Google App Engine does not support threads.')

    def stopSplineSelfUpdateThread(self):
        if self._splineThread is not None:
            self._splineThread.stopUpdating()
            self._indicator.setEnabled(False)
            self.getApplication().notifyAll()

    _splineThread = None
    _indicator = None

    class SelfUpdateSplineThread(Window.Thread, Serializable):
        _chart = None

        def __init__(self, chart):
            self._chart = chart

        _keepUpdating = True

        def stopUpdating(self):
            self._keepUpdating = False
            print 'stopUpdating ' + self._keepUpdating

        def keepUpdating(self):
            return self._keepUpdating

        def run(self):
            while self.keepUpdating():
                # Sleep for 1 second
                try:
                    self.Thread.sleep(1000)
                except self.InterruptedException, e:
                    print 'InterruptedException occured. Exception message ' + e.getMessage()
                seriesData = self._chart.getSeries('Random Data')
                seriesData.addPoint(DateTimePoint(seriesData, Date(), self.Math.random()), True)
                print 'Inside run() keepUpdating ' + self._keepUpdating

    @classmethod
    def getUpdatedDate(cls, dt, milliseconds):
        cal = Calendar.getInstance()
        cal.setTimeInMillis(dt.getTime() + milliseconds)
        return cal.getTime()

    def showSplineWithPlotBands(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setType(SeriesType.SPLINE)
        chartConfig.getTitle().setText('Wind speed during two days')
        chartConfig.getSubtitle().setText('October 6th and 7th 2009 at two locations in Vik i Sogn, Norway')
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' return \'\' + $wnd.Highcharts.dateFormat(\'%e. %b %Y, %H:00\', this.x) +\': \'+ this.y +\' m/s\'; ' + '}')
        xAxis = DateTimeAxis()
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Wind speed (m/s)'))
        yAxis.setMin(0.0)
        yAxis.setMinorGrid(MinorGrid())
        yAxis.getMinorGrid().setLineWidth(0)
        yAxis.setGrid(Grid())
        yAxis.getGrid().setLineWidth(0)
        numberBand = NumberPlotBand('Light air')
        numberBand.setRange(NumberRange(0.3, 1.5))
        numberBand.setColor(RGBA(68, 170, 213, 0.1))
        numberBand.setLabel(PlotLabel('Light air'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('Light breeze')
        numberBand.setRange(NumberRange(1.5, 3.3))
        numberBand.setColor(RGBA(0, 0, 0, 0.0))
        numberBand.setLabel(PlotLabel('Light breeze'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('Gentle breeze')
        numberBand.setRange(NumberRange(3.3, 5.5))
        numberBand.setColor(RGBA(68, 170, 213, 0.1))
        numberBand.setLabel(PlotLabel('Gentle breeze'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('Moderate breeze')
        numberBand.setRange(NumberRange(5.5, 8.0))
        numberBand.setColor(RGBA(0, 0, 0, 0.0))
        numberBand.setLabel(PlotLabel('Moderate breeze'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('Fresh breeze')
        numberBand.setRange(NumberRange(8.0, 11.0))
        numberBand.setColor(RGBA(68, 170, 213, 0.1))
        numberBand.setLabel(PlotLabel('Fresh breeze'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('Strong breeze')
        numberBand.setRange(NumberRange(11.0, 14.0))
        numberBand.setColor(RGBA(0, 0, 0, 0.0))
        numberBand.setLabel(PlotLabel('Strong breeze'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        numberBand = NumberPlotBand('High wind')
        numberBand.setRange(NumberRange(14.0, 15.0))
        numberBand.setColor(RGBA(68, 170, 213, 0.1))
        numberBand.setLabel(PlotLabel('High wind'))
        numberBand.getLabel().setStyle('{ color: \'#606060\' }')
        yAxis.getPlotBands().add(numberBand)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        splineCfg = SplineConfig()
        splineCfg.setLineWidth(4)
        splineCfg.setHoverState(SeriesState())
        splineCfg.getHoverState().setLineWidth(5)
        symbolMarker = SymbolMarker(False)
        splineCfg.setMarker(symbolMarker)
        symbolMarker.setSymbol(Symbol.CIRCLE)
        symbolMarker.setHoverState(MarkerState())
        symbolMarker.getHoverState().setEnabled(True)
        symbolMarker.getHoverState().setRadius(5)
        symbolMarker.getHoverState().setLineWidth(1)
        splineCfg.setPointStart(self.getPointStartDate(2009, 8, 6))
        splineCfg.setPointInterval(3600000.0)
        chartConfig.addSeriesConfig(splineCfg)
        chart = InvientCharts(chartConfig)
        series = DateTimeSeries('Hestavollane', splineCfg, True)
        series.setSeriesPoints(self.getDateTimePoints(series, 4.3, 5.1, 4.3, 5.2, 5.4, 4.7, 3.5, 4.1, 5.6, 7.4, 6.9, 7.1, 7.9, 7.9, 7.5, 6.7, 7.7, 7.7, 7.4, 7.0, 7.1, 5.8, 5.9, 7.4, 8.2, 8.5, 9.4, 8.1, 10.9, 10.4, 10.9, 12.4, 12.1, 9.5, 7.5, 7.1, 7.5, 8.1, 6.8, 3.4, 2.1, 1.9, 2.8, 2.9, 1.3, 4.4, 4.2, 3.0, 3.0))
        chart.addSeries(series)
        series = DateTimeSeries('Voll', splineCfg, True)
        series.setSeriesPoints(self.getDateTimePoints(series, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.3, 0.0, 0.0, 0.4, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 1.2, 1.7, 0.7, 2.9, 4.1, 2.6, 3.7, 3.9, 1.7, 2.3, 3.0, 3.3, 4.8, 5.0, 4.8, 5.0, 3.2, 2.0, 0.9, 0.4, 0.3, 0.5, 0.4))
        chart.addSeries(series)
        self.addChart(chart)

    def showCombination(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getTitle().setText('Combination chart')
        tooltip = Tooltip()
        tooltip.setFormatterJsFunc('function() {' + ' if (this.point.name) { // the pie chart ' + '   return this.point.name +\': \'+ this.y +\' fruits\'; ' + ' } else {' + '   return this.x  +\': \'+ this.y; ' + ' } ' + '}')
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Apples', 'Oranges', 'Pears', 'Bananas', 'Plums'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setAllowDecimals(False)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chart = InvientCharts(chartConfig)
        seriesData = XYSeries('Jane', SeriesType.COLUMN)
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 2, 1, 3, 4))
        chart.addSeries(seriesData)
        seriesData = XYSeries('John', SeriesType.COLUMN)
        seriesData.setSeriesPoints(self.getPoints(seriesData, 2, 3, 5, 7, 6))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Joe', SeriesType.COLUMN)
        seriesData.setSeriesPoints(self.getPoints(seriesData, 4, 3, 3, 9, 0))
        chart.addSeries(seriesData)
        seriesData = XYSeries('Average', SeriesType.SPLINE)
        seriesData.setSeriesPoints(self.getPoints(seriesData, 3, 2.67, 3, 6.33, 3.33))
        chart.addSeries(seriesData)
        # Series Total consumption
        pieCfg = PieConfig()
        pieCfg.setCenterX(100)
        pieCfg.setCenterY(80)
        pieCfg.setSize(100)
        pieCfg.setShowInLegend(False)
        pieCfg.setDataLabel(PieDataLabel())
        pieCfg.getDataLabel().setEnabled(False)
        totalConsumpSeriesData = XYSeries('Total consumption', SeriesType.PIE, pieCfg)
        config = PointConfig(RGB(69, 114, 167))
        point = DecimalPoint(totalConsumpSeriesData, 'Jane', 13, config)
        totalConsumpSeriesData.addPoint(point)
        config = PointConfig(RGB(170, 70, 67))
        point = DecimalPoint(totalConsumpSeriesData, 'John', 23, config)
        totalConsumpSeriesData.addPoint(point)
        config = PointConfig(RGB(137, 165, 78))
        point = DecimalPoint(totalConsumpSeriesData, 'Joe', 19, config)
        totalConsumpSeriesData.addPoint(point)
        chartLabel = ChartLabel()
        chartLabel.addLabel(ChartLabelItem('Total fruit consumption', '{ left: \'40px\', top: \'8px\', color: \'black\' }'))
        chartConfig.setChartLabel(chartLabel)
        chart.addSeries(totalConsumpSeriesData)
        self.addChart(chart)

    def showCombinationMultipleAxes(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getTitle().setText('Average Monthly Weather Data for Tokyo')
        chartConfig.getSubtitle().setText('Source: WorldClimate.com')
        chartConfig.getTooltip().setFormatterJsFunc('function() {' + ' var unit = { ' + '         \'Rainfall\': \'mm\',' + '         \'Temperature\': \'°C\',' + '         \'Sea-Level Pressure\': \'mb\'' + ' }[this.series.name];' + '   return \'\' + this.x + \': \' + this.y + \' \' + unit; ' + '}')
        legend = Legend()
        legend.setLayout(Layout.VERTICAL)
        legend.setPosition(Position())
        legend.getPosition().setAlign(HorzAlign.LEFT)
        legend.getPosition().setVertAlign(VertAlign.TOP)
        legend.getPosition().setX(120)
        legend.getPosition().setY(80)
        legend.setFloating(True)
        legend.setBackgroundColor(RGB(255, 255, 255))
        chartConfig.setLegend(legend)
        xAxis = CategoryAxis()
        xAxis.setCategories(Arrays.asList('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        # Multiple axes
        temperatureAxis = NumberYAxis()
        temperatureAxis.setAllowDecimals(False)
        temperatureAxis.setLabel(YAxisDataLabel())
        temperatureAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value +\'°C\'; ' + '}')
        temperatureAxis.getLabel().setStyle('{ color: \'#89A54E\' }')
        temperatureAxis.setTitle(AxisTitle('Temperature'))
        temperatureAxis.getTitle().setStyle(' { color: \'#89A54E\' }')
        temperatureAxis.setOpposite(True)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(temperatureAxis)
        # secondary y-axis
        rainfallAxis = NumberYAxis()
        rainfallAxis.setGrid(Grid())
        rainfallAxis.getGrid().setLineWidth(0)
        rainfallAxis.setTitle(AxisTitle('Rainfall'))
        rainfallAxis.getTitle().setStyle(' { color: \'#4572A7\' }')
        rainfallAxis.setLabel(YAxisDataLabel())
        rainfallAxis.getLabel().setStyle('{ color: \'#4572A7\' }')
        rainfallAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value +\' mm\'; ' + '}')
        yAxesSet.add(rainfallAxis)
        # tertiary y-axis
        sealevelPressureAxis = NumberYAxis()
        sealevelPressureAxis.setGrid(Grid())
        sealevelPressureAxis.getGrid().setLineWidth(0)
        sealevelPressureAxis.setTitle(AxisTitle('Sea-Level Pressure'))
        sealevelPressureAxis.getTitle().setStyle(' { color: \'#AA4643\' }')
        sealevelPressureAxis.setLabel(YAxisDataLabel())
        sealevelPressureAxis.getLabel().setStyle('{ color: \'#AA4643\' }')
        sealevelPressureAxis.getLabel().setFormatterJsFunc('function() {' + ' return this.value +\' mb\'; ' + '}')
        sealevelPressureAxis.setOpposite(True)
        yAxesSet.add(sealevelPressureAxis)
        chartConfig.setYAxes(yAxesSet)
        chart = InvientCharts(chartConfig)
        # Configuration of Rainfall series
        colCfg = ColumnConfig()
        colCfg.setColor(RGB(69, 114, 167))
        # Rainfall series
        rainfallSeriesData = XYSeries('Rainfall', SeriesType.COLUMN, colCfg)
        rainfallSeriesData.setSeriesPoints(self.getPoints(rainfallSeriesData, 49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4))
        rainfallSeriesData.setYAxis(rainfallAxis)
        chart.addSeries(rainfallSeriesData)
        # Configuration of Sealevel series
        seaLevelSplineCfg = SplineConfig()
        seaLevelSplineCfg.setColor(RGB(170, 70, 67))
        seaLevelSplineCfg.setMarker(SymbolMarker(False))
        seaLevelSplineCfg.setDashStyle(DashStyle.SHORT_DOT)
        # Sealevel series
        seaLevelSeriesData = XYSeries('Sea-Level Pressure', SeriesType.SPLINE, seaLevelSplineCfg)
        seaLevelSeriesData.setSeriesPoints(self.getPoints(seaLevelSeriesData, 1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7))
        seaLevelSeriesData.setYAxis(sealevelPressureAxis)
        chart.addSeries(seaLevelSeriesData)
        # Configuration of Temperature series
        tempSplineCfg = SplineConfig()
        tempSplineCfg.setColor(RGB(137, 165, 78))
        # Temperature series
        tempSeriesData = XYSeries('Temperature', SeriesType.SPLINE, tempSplineCfg)
        tempSeriesData.setSeriesPoints(self.getPoints(tempSeriesData, 7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6))
        chart.addSeries(tempSeriesData)
        self.addChart(chart)

    def showTimeSeriesZoomable(self):
        chartConfig = InvientChartsConfig()
        chartConfig.getGeneralChartConfig().setZoomType(ZoomType.X)
        chartConfig.getGeneralChartConfig().setSpacing(Spacing())
        chartConfig.getGeneralChartConfig().getSpacing().setRight(20)
        chartConfig.getSubtitle().setText('Click and drag in the plot area to zoom in')
        xAxis = DateTimeAxis()
        xAxis.setMaxZoom(14 * 24 * 3600000)
        xAxesSet = LinkedHashSet()
        xAxesSet.add(xAxis)
        chartConfig.setXAxes(xAxesSet)
        yAxis = NumberYAxis()
        yAxis.setTitle(AxisTitle('Exchange rate'))
        yAxis.setMin(0.6)
        yAxis.setStartOnTick(True)
        yAxis.setShowFirstLabel(False)
        yAxesSet = LinkedHashSet()
        yAxesSet.add(yAxis)
        chartConfig.setYAxes(yAxesSet)
        chartConfig.getTooltip().setShared(True)
        chartConfig.getLegend().setEnabled(False)
        # Set plot options
        areaCfg = AreaConfig()
        colorStops = list()
        colorStops.add(LinearColorStop(0, RGB(69, 114, 167)))
        colorStops.add(LinearColorStop(1, RGBA(2, 0, 0, 0)))
        # Fill color
        areaCfg.setFillColor(Gradient.LinearGradient(0, 0, 0, 300, colorStops))
        areaCfg.setLineWidth(1)
        areaCfg.setShadow(False)
        areaCfg.setHoverState(SeriesState())
        areaCfg.getHoverState().setLineWidth(1)
        areaCfg.setMarker(marker = SymbolMarker(False))
        marker.setHoverState(MarkerState())
        marker.getHoverState().setEnabled(True)
        marker.getHoverState().setRadius(5)
        chartConfig.addSeriesConfig(areaCfg)
        chart = InvientCharts(chartConfig)
        # Area configuration
        serieaAreaCfg = AreaConfig()
        serieaAreaCfg.setPointStart(self.getPointStartDate(2006, 0, 1))
        serieaAreaCfg.setPointInterval(24 * 3600 * 1000.0)
        # Series
        dateTimeSeries = DateTimeSeries('USD to EUR', SeriesType.AREA, serieaAreaCfg)
        dateTimeSeries.addPoint(self.getDateTimeSeriesPoints(dateTimeSeries))
        chart.addSeries(dateTimeSeries)
        self.addChart(chart)

    def addChart(self, *args):
        _0 = args
        _1 = len(args)
        if _1 == 1:
            chart, = _0
            self.addChart(chart, False, True)
        elif _1 == 3:
            chart, isPrepend, isRegisterEvents = _0
            self.addChart(chart, isPrepend, isRegisterEvents, True)
        elif _1 == 4:
            chart, isPrepend, isRegisterEvents, isRegisterSVGEvent = _0
            self.addChart(chart, isPrepend, isRegisterEvents, isRegisterSVGEvent, True)
        elif _1 == 5:
            chart, isPrepend, isRegisterEvents, isRegisterSVGEvent, isSetHeight = _0
            if isRegisterEvents:
                self.registerEvents(chart)
            chart.setSizeFull()
            chart.setStyleName('v-chart-min-width')
            if isSetHeight:
                chart.setHeight('410px')
            if isPrepend:
                self._rightLayout.setStyleName('v-chart-master-detail')
                self._rightLayout.addComponentAsFirst(chart)
            else:
                self._rightLayout.removeStyleName('v-chart-master-detail')
                self.emptyEventLog()
                self._rightLayout.removeAllComponents()
                # Add chart
                self._rightLayout.addComponent(chart)
                # Add "Get SVG" button and register SVG available event
                if isRegisterSVGEvent:
                    self.registerSVGAndPrintEvent(chart)
                # Server events log
                self._rightLayout.addComponent(Label('Events received by the server:'))
                self._rightLayout.addComponent(self._eventLog)
        else:
            raise ARGERROR(1, 5)

    # add events

    def registerSVGAndPrintEvent(self, chart):
        gridLayout = GridLayout(2, 1)
        gridLayout.setWidth('100%')
        gridLayout.setSpacing(True)
        gridLayout.addComponent(svgBtn = Button('Get SVG'))
        gridLayout.setComponentAlignment(svgBtn, Alignment.MIDDLE_RIGHT)
        gridLayout.addComponent(printBtn = Button('Print'))
        gridLayout.setComponentAlignment(printBtn, Alignment.MIDDLE_LEFT)
        self._rightLayout.addComponent(gridLayout)

        class _4_(Button.ClickListener):

            def buttonClick(self, event):

                class _4_(InvientCharts.ChartSVGAvailableListener):

                    def svgAvailable(self, chartSVGAvailableEvent):
                        InvientChartsDemoWin_this.logEventInfo('[svgAvailable]' + ' svg -> ' + chartSVGAvailableEvent.getSVG())

                _4_ = _4_()
                self.chart.addListener(_4_)

        _4_ = _4_()
        svgBtn.addListener(_4_)

        class _6_(Button.ClickListener):

            def buttonClick(self, event):
                self.chart.print_()

        _6_ = _6_()
        printBtn.addListener(_6_)

    def registerEvents(self, chart):

        class _7_(InvientCharts.ChartClickListener):

            def chartClick(self, chartClickEvent):
                InvientChartsDemoWin_this.logEventInfo('chartClick', chartClickEvent.getPoint().getX(), chartClickEvent.getPoint().getY(), chartClickEvent.getMousePosition().getMouseX(), chartClickEvent.getMousePosition().getMouseY())

        _7_ = _7_()
        chart.addListener(_7_)
        if chart.getConfig().getGeneralChartConfig().getZoomType() is not None:

            class _8_(InvientCharts.ChartZoomListener):

                def chartZoom(self, chartZoomEvent):
                    InvientChartsDemoWin_this.logEventInfo('chartSelection', chartZoomEvent.getChartArea().getxAxisMin(), chartZoomEvent.getChartArea().getxAxisMax(), chartZoomEvent.getChartArea().getyAxisMin(), chartZoomEvent.getChartArea().getyAxisMax())

            _8_ = _8_()
            chart.addListener(_8_)

            class _9_(InvientCharts.ChartResetZoomListener):

                def chartResetZoom(self, chartResetZoomEvent):
                    InvientChartsDemoWin_this.logEventInfo('[chartSelectionReset]')

            _9_ = _9_()
            chart.addListener(_9_)

        class _10_(InvientCharts.SeriesClickListerner):

            def seriesClick(self, seriesClickEvent):
                EVENT_NAME = 'seriesClick'
                if isinstance(seriesClickEvent.getNearestPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, seriesClickEvent.getSeries().getName(), None, seriesClickEvent.getNearestPoint().getX(), seriesClickEvent.getNearestPoint().getY(), seriesClickEvent.getMousePosition().getMouseX(), seriesClickEvent.getMousePosition().getMouseY())
                else:
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, seriesClickEvent.getSeries().getName(), None, seriesClickEvent.getNearestPoint().getX(), seriesClickEvent.getNearestPoint().getY(), seriesClickEvent.getMousePosition().getMouseX(), seriesClickEvent.getMousePosition().getMouseY())

        _10_ = _10_()
        chart.addListener(_10_)

        class _11_(InvientCharts.SeriesHideListerner):

            def seriesHide(self, seriesHideEvent):
                InvientChartsDemoWin_this.logEventInfo('seriesHide', seriesHideEvent.getSeries().getName())

        _11_ = _11_()
        chart.addListener(_11_)

        class _12_(InvientCharts.SeriesShowListerner):

            def seriesShow(self, seriesShowEvent):
                InvientChartsDemoWin_this.logEventInfo('seriesShow', seriesShowEvent.getSeries().getName())

        _12_ = _12_()
        chart.addListener(_12_)

        class _13_(InvientCharts.SeriesLegendItemClickListerner):

            def seriesLegendItemClick(self, seriesLegendItemClickEvent):
                InvientChartsDemoWin_this.logEventInfo('seriesLegendItemClick', seriesLegendItemClickEvent.getSeries().getName())

        _13_ = _13_()
        chart.addListener(_13_)

        class _14_(InvientCharts.PointClickListener):

            def pointClick(self, pointClickEvent):
                EVENT_NAME = 'pointClick'
                if isinstance(pointClickEvent.getPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointClickEvent.getPoint().getSeries().getName(), pointClickEvent.getCategory(), pointClickEvent.getPoint().getX(), pointClickEvent.getPoint().getY(), pointClickEvent.getMousePosition().getMouseX(), pointClickEvent.getMousePosition().getMouseY())
                else:
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointClickEvent.getPoint().getSeries().getName(), pointClickEvent.getCategory(), pointClickEvent.getPoint().getX(), pointClickEvent.getPoint().getY(), pointClickEvent.getMousePosition().getMouseX(), pointClickEvent.getMousePosition().getMouseY())

        _14_ = _14_()
        chart.addListener(_14_)

        class _15_(InvientCharts.PointRemoveListener):

            def pointRemove(self, pointRemoveEvent):
                EVENT_NAME = 'pointRemove'
                if isinstance(pointRemoveEvent.getPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointRemoveEvent.getPoint().getSeries().getName(), pointRemoveEvent.getCategory(), pointRemoveEvent.getPoint().getX(), pointRemoveEvent.getPoint().getY())
                else:
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointRemoveEvent.getPoint().getSeries().getName(), pointRemoveEvent.getCategory(), pointRemoveEvent.getPoint().getX(), pointRemoveEvent.getPoint().getY())

        _15_ = _15_()
        chart.addListener(_15_)

        class _16_(InvientCharts.PointSelectListener):

            def pointSelected(self, pointSelectEvent):
                EVENT_NAME = 'pointSelected'
                if isinstance(pointSelectEvent.getPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointSelectEvent.getPoint().getSeries().getName(), pointSelectEvent.getCategory(), pointSelectEvent.getPoint().getX(), pointSelectEvent.getPoint().getY())
                else:
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointSelectEvent.getPoint().getSeries().getName(), pointSelectEvent.getCategory(), pointSelectEvent.getPoint().getX(), pointSelectEvent.getPoint().getY())

        _16_ = _16_()
        chart.addListener(_16_)

        class _17_(InvientCharts.PointUnselectListener):

            def pointUnSelect(self, pointUnSelectEvent):
                EVENT_NAME = 'pointUnSelected'
                if isinstance(pointUnSelectEvent.getPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointUnSelectEvent.getPoint().getSeries().getName(), pointUnSelectEvent.getCategory(), pointUnSelectEvent.getPoint().getX(), pointUnSelectEvent.getPoint().getY())
                else:
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, pointUnSelectEvent.getPoint().getSeries().getName(), pointUnSelectEvent.getCategory(), pointUnSelectEvent.getPoint().getX(), pointUnSelectEvent.getPoint().getY())

        _17_ = _17_()
        chart.addListener(_17_)

        class _18_(InvientCharts.PieChartLegendItemClickListener):

            def legendItemClick(self, legendItemClickEvent):
                EVENT_NAME = 'pieLegendItemClick'
                if isinstance(legendItemClickEvent.getPoint(), DecimalPoint):
                    InvientChartsDemoWin_this.logEventInfo(EVENT_NAME, legendItemClickEvent.getPoint().getSeries().getName(), None, legendItemClickEvent.getPoint().getX(), legendItemClickEvent.getPoint().getY())

        _18_ = _18_()
        chart.addListener(_18_)

    @classmethod
    def getPointStartDate(cls, year, month, day):
        cal = GregorianCalendar.getInstance()
        cal.set(Calendar.YEAR, year)
        cal.set(Calendar.MONTH, month)
        cal.set(Calendar.DAY_OF_MONTH, day)
        cal.set(Calendar.HOUR, 0)
        cal.set(Calendar.MINUTE, 0)
        cal.set(Calendar.SECOND, 0)
        cal.set(Calendar.MILLISECOND, 0)
        return cal.getTimeInMillis()

    @classmethod
    def getDateZeroTime(cls, year, month, day):
        cal = GregorianCalendar.getInstance()
        cal.set(Calendar.YEAR, year)
        cal.set(Calendar.MONTH, month)
        cal.set(Calendar.DAY_OF_MONTH, day)
        cls.setZeroTime(cal)
        return cal.getTime()

    @classmethod
    def setZeroTime(cls, cal):
        cal.set(Calendar.HOUR, 0)
        cal.set(Calendar.MINUTE, 0)
        cal.set(Calendar.SECOND, 0)
        cal.set(Calendar.MILLISECOND, 0)

    def getDateTimePoints(self, series, *values):
        points = LinkedHashSet()
        for value in values:
            points.add(DateTimePoint(series, value))
        return points

    @classmethod
    def getPoints(cls, *args):
        _0 = args
        _1 = len(args)
        if _1 == 2:
            series, values = _0
            points = LinkedHashSet()
            for value in values:
                points.add(DecimalPoint(series, value))
            return points
            series, values = _0
            points = LinkedHashSet()
            for value in values:
                y = None
                if len(value) == 0:
                    continue
                if len(value) == 2:
                    x = value[0]
                    y = value[1]
                else:
                    x = value[0]
                points.add(DecimalPoint(series, x, y))
            return points
        else:
            raise ARGERROR(2, 2)

    @classmethod
    def getFormattedTimestamp(cls, dt):
        if dt is None:
            return None
        format = SimpleDateFormat('yy/MM/dd hh:mm:ss')
        return format.format(dt)

    @classmethod
    def getCurrFormattedTimestamp(cls):
        return cls.getFormattedTimestamp(Date())

    class ChartName(object):
        BASIC = ['Basic']
        DONUT = ['Donut']
        CLICK_TO_ADD_POINT = ['Click to add a point']
        MASTER_DETAIL = ['Master-detail']
        TIMESERIES_ZOOMABLE = ['Time series, zoomable']
        WITH_DATA_LABELS = ['With data labels']
        STACKED = ['Stacked']
        WITH_NEGATIVE_STACK = ['With negative stack']
        WITH_NEGATIVE_VALUES = ['With negative values']
        STACKED_AND_GROUPED = ['Stacked and grouped']
        STACKED_PERCENT = ['Stacked percentage']
        WITH_ROTATED_LABELS = ['With rotated labels']
        WITH_MISSING_POINTS = ['With missing points']
        INVERTED_AXES = ['Inverted axes']
        WITH_LEGEND = ['With legend']
        WITH_PLOTBANDS = ['With plot bands']
        WITH_SYMBOLS = ['With symbols']
        UPDATING_EACH_SECOND = ['Updating each second']
        COMBINATION_COLUMN_LINE_AND_PIE = ['Column, spline and pie']
        PERCENTAGE = ['Percentage']
        SCATTER_WITH_REGRESSION_LINE = ['Scatter with regression line']
        MULTIPLE_AXES = ['Multiple axes']
        _name = None

        def __init__(self, name):
            self._name = name

        def getName(self):
            return self._name

        _values = [BASIC, DONUT, CLICK_TO_ADD_POINT, MASTER_DETAIL, TIMESERIES_ZOOMABLE, WITH_DATA_LABELS, STACKED, WITH_NEGATIVE_STACK, WITH_NEGATIVE_VALUES, STACKED_AND_GROUPED, STACKED_PERCENT, WITH_ROTATED_LABELS, WITH_MISSING_POINTS, INVERTED_AXES, WITH_LEGEND, WITH_PLOTBANDS, WITH_SYMBOLS, UPDATING_EACH_SECOND, COMBINATION_COLUMN_LINE_AND_PIE, PERCENTAGE, SCATTER_WITH_REGRESSION_LINE, MULTIPLE_AXES]

        @classmethod
        def values(cls):
            return cls._enum_values[:]

    ChartName._enum_values = [ChartName(*v) for v in ChartName._enum_values]

    def getChartName(self, chartNameString):
        for chartName in self.ChartName.values():
            if chartNameString.equalsIgnoreCase(chartName.getName()):
                return chartName
        return None

    class DemoSeriesType(object):
        LINE = [SeriesType.LINE, 'Line']
        SPLINE = [SeriesType.SPLINE, 'Spline']
        SCATTER = [SeriesType.SCATTER, 'Scatter']
        AREA = [SeriesType.AREA, 'Area - Line']
        AREASPLINE = [SeriesType.AREASPLINE, 'Area - Spline']
        BAR = [SeriesType.BAR, 'Bar']
        COLUMN = [SeriesType.COLUMN, 'Column']
        PIE = [SeriesType.PIE, 'Pie']
        COMBINATION = [SeriesType.COMMONSERIES, 'Combination']
        _seriesType = None
        _name = None

        def __init__(self, seriesType, name):
            self._seriesType = seriesType
            self._name = name

        def getSeriesType(self):
            return self._seriesType

        def getName(self):
            return self._name

        _values = [LINE, SPLINE, SCATTER, AREA, AREASPLINE, BAR, COLUMN, PIE, COMBINATION]

        @classmethod
        def values(cls):
            return cls._enum_values[:]

    DemoSeriesType._enum_values = [DemoSeriesType(*v) for v in DemoSeriesType._enum_values]

    def getDemoSeriesType(self, demoSeriesTypeName):
        for demoSeriesType in self.DemoSeriesType.values():
            if demoSeriesTypeName.equalsIgnoreCase(demoSeriesType.getName()):
                return demoSeriesType
        return None

    def createChartsTree(self):
        tree = Tree('Chart Type')
        tree.setContainerDataSource(self.getContainer())
        tree.setImmediate(True)
        tree.setItemCaptionPropertyId(self._TREE_ITEM_CAPTION_PROP_ID)
        tree.setItemCaptionMode(Tree.ITEM_CAPTION_MODE_PROPERTY)
        tree.setNullSelectionAllowed(False)
        for id in tree.rootItemIds():
            tree.expandItemsRecursively(id)

        class _19_(Tree.ValueChangeListener):

            def valueChange(self, event):
                try:
                    selectedId = event.getProperty().getValue()
                    if self.tree.getParent(selectedId) is not None:
                        parentId = self.tree.getParent(selectedId)
                        demoSeriesTypeName = self.tree.getContainerProperty(parentId, InvientChartsDemoWin_this._TREE_ITEM_CAPTION_PROP_ID).getValue()
                        seriesInstanceName = self.tree.getContainerProperty(selectedId, InvientChartsDemoWin_this._TREE_ITEM_CAPTION_PROP_ID).getValue()
                        print 'parent : ' + demoSeriesTypeName + ', selected : ' + seriesInstanceName
                        InvientChartsDemoWin_this.showChart(demoSeriesTypeName, seriesInstanceName)
                    else:
                        demoSeriesTypeName = self.tree.getContainerProperty(selectedId, InvientChartsDemoWin_this._TREE_ITEM_CAPTION_PROP_ID).getValue()
                        print 'Selected ' + demoSeriesTypeName
                        InvientChartsDemoWin_this.showChartInstancesForSeriesType(demoSeriesTypeName)
                except Exception, e:
                    e.printStackTrace()

        _19_ = _19_()
        tree.addListener(_19_)
        return tree

    def showChartInstancesForSeriesType(self, demoSeriesTypeName):
        self._rightLayout.removeAllComponents()
        demoCharts = self.getDemoCharts(self.getDemoSeriesType(demoSeriesTypeName))
        for chartName in demoCharts:
            btn = None
            self._rightLayout.addComponent(


            class _20_(Button.ClickListener):

                def buttonClick(self, event):
                    InvientChartsDemoWin_this._navTree.select(self.demoSeriesTypeName + InvientChartsDemoWin_this._SEPARATOR + event.getButton().getCaption())


            _20_ = _20_()
            Button(chartName.getName(), _20_)
            btn = _20_)
            btn.setWidth('200px')

    _SEPARATOR = '|'

    def getContainer(self):
        container = HierarchicalContainer()
        container.addContainerProperty(self._TREE_ITEM_CAPTION_PROP_ID, str, '')
        for demoSeriesType in self.DemoSeriesType.values():
            itemId = demoSeriesType.getName()
            item = container.addItem(itemId)
            item.getItemProperty(self._TREE_ITEM_CAPTION_PROP_ID).setValue(demoSeriesType.getName())
            container.setChildrenAllowed(itemId, True)
            # add child
            self.addChartNamesForSeriesType(container, itemId, demoSeriesType)
        return container

    def addChartNamesForSeriesType(self, container, parentId, demoSeriesType):
        for chartName in self.getDemoCharts(demoSeriesType):
            childItemId = demoSeriesType.getName() + self._SEPARATOR + chartName.getName()
            childItem = container.addItem(childItemId)
            childItem.getItemProperty(self._TREE_ITEM_CAPTION_PROP_ID).setValue(chartName.getName())
            container.setParent(childItemId, parentId)
            container.setChildrenAllowed(childItemId, False)

    def getDemoCharts(self, demoSeriesType):
        chartNames = list()
        _0 = demoSeriesType
        _1 = False
        while True:
            if _0 == self.LINE:
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.WITH_DATA_LABELS)
                chartNames.add(self.ChartName.TIMESERIES_ZOOMABLE)
                chartNames.add(self.ChartName.MASTER_DETAIL)
                chartNames.add(self.ChartName.CLICK_TO_ADD_POINT)
                break
            if (_1 is True) or (_0 == self.BAR):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.STACKED)
                chartNames.add(self.ChartName.WITH_NEGATIVE_STACK)
                break
            if (_1 is True) or (_0 == self.COLUMN):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.WITH_NEGATIVE_VALUES)
                chartNames.add(self.ChartName.STACKED)
                chartNames.add(self.ChartName.STACKED_AND_GROUPED)
                chartNames.add(self.ChartName.STACKED_PERCENT)
                chartNames.add(self.ChartName.WITH_ROTATED_LABELS)
                break
            if (_1 is True) or (_0 == self.AREA):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.WITH_NEGATIVE_VALUES)
                chartNames.add(self.ChartName.STACKED)
                chartNames.add(self.ChartName.PERCENTAGE)
                chartNames.add(self.ChartName.WITH_MISSING_POINTS)
                chartNames.add(self.ChartName.INVERTED_AXES)
                break
            if (_1 is True) or (_0 == self.AREASPLINE):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                break
            if (_1 is True) or (_0 == self.PIE):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.WITH_LEGEND)
                chartNames.add(self.ChartName.DONUT)
                break
            if (_1 is True) or (_0 == self.SCATTER):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                break
            if (_1 is True) or (_0 == self.SPLINE):
                _1 = True
                chartNames.add(self.ChartName.BASIC)
                chartNames.add(self.ChartName.WITH_PLOTBANDS)
                chartNames.add(self.ChartName.WITH_SYMBOLS)
                chartNames.add(self.ChartName.UPDATING_EACH_SECOND)
                break
            if (_1 is True) or (_0 == self.COMBINATION):
                _1 = True
                chartNames.add(self.ChartName.COMBINATION_COLUMN_LINE_AND_PIE)
                chartNames.add(self.ChartName.SCATTER_WITH_REGRESSION_LINE)
                chartNames.add(self.ChartName.MULTIPLE_AXES)
                break
            break
        return chartNames

    def logEventInfo(self, *args):
        _0 = args
        _1 = len(args)
        if _1 == 1:
            eventInfo, = _0
            self.logEventInfo(eventInfo, True)
        elif _1 == 2:
            if isinstance(_0[1], boolean):
                eventInfo, isAppend = _0
                self._eventLog.setReadOnly(False)
                if isAppend:
                    self._eventLog.setValue('[' + self.getCurrFormattedTimestamp() + '] ' + eventInfo + '\n' + self._eventLog.getValue())
                else:
                    self._eventLog.setValue('')
                self._eventLog.setReadOnly(True)
            else:
                eventName, seriesName = _0
                sb = self.StringBuilder('')
                sb.append('[' + eventName + ']')
                sb.append(' series -> ' + seriesName)
                self.logEventInfo(str(sb))
        elif _1 == 5:
            if isinstance(_0[1], float):
                if isinstance(_0[3], float):
                    eventName, xAxisMin, xAxisMax, yAxisMin, yAxisMax = _0
                    sb = self.StringBuilder('')
                    sb.append('[' + eventName + ']')
                    sb.append(', xAxisMin -> ' + xAxisMin)
                    sb.append(', xAxisMax -> ' + xAxisMax)
                    sb.append(', yAxisMin -> ' + yAxisMin)
                    sb.append(', yAxisMax -> ' + yAxisMax)
                    self.logEventInfo(str(sb))
                else:
                    eventName, xAxisPos, yAxisPos, mouseX, mouseY = _0
                    sb = self.StringBuilder('')
                    sb.append('[' + eventName + ']')
                    sb.append(', xAxisPos -> ' + xAxisPos)
                    sb.append(', yAxisPos -> ' + yAxisPos)
                    sb.append(', mouseX -> ' + mouseX)
                    sb.append(', mouseY -> ' + mouseY)
                    self.logEventInfo(str(sb))
            else:
                if isinstance(_0[3], Date):
                    eventName, seriesName, category, x, y = _0
                    self.logEventInfo(eventName, seriesName, category, x, y, None, None)
                else:
                    eventName, seriesName, category, x, y = _0
                    self.logEventInfo(eventName, seriesName, category, x, y, None, None)
        elif _1 == 7:
            if isinstance(_0[3], Date):
                eventName, seriesName, category, x, y, mouseX, mouseY = _0
                self.logStringEventInfo(eventName, seriesName, category, str(x) if x is not None else None, str(y) if y is not None else None, str(mouseX) if mouseX is not None else None, str(mouseY) if mouseY is not None else None)
            else:
                eventName, seriesName, category, x, y, mouseX, mouseY = _0
                self.logStringEventInfo(eventName, seriesName, category, str(x) if x is not None else None, str(y) if y is not None else None, str(mouseX) if mouseX is not None else None, str(mouseY) if mouseY is not None else None)
        else:
            raise ARGERROR(1, 7)

    def logStringEventInfo(self, eventName, seriesName, category, x, y, mouseX, mouseY):
        sb = self.StringBuilder('')
        sb.append('[' + eventName + ']')
        sb.append(' series -> ' + seriesName)
        if category is not None and len(category) > 0:
            sb.append(', category -> ' + category)
        if x is not None:
            sb.append(', x -> ' + x)
        if y is not None:
            sb.append(', y -> ' + y)
        if mouseX is not None:
            sb.append(', mouseX -> ' + mouseX)
        if mouseY is not None:
            sb.append(', mouseY -> ' + mouseY)
        self.logEventInfo(str(sb))

    def emptyEventLog(self):
        self.logEventInfo('', False)

    _scatterMaleData = None
    _scatterFemaleData = None

    def getScatterFemalePoints(self, series):
        if self._scatterFemaleData is not None:
            return self._scatterFemaleData
        # Initialize data
        self._scatterFemaleData = self.getPoints(series, [161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6], [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2], [172.5, 55.2], [170.9, 54.2], [172.9, 62.5], [153.4, 42.0], [160.0, 50.0], [147.2, 49.8], [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8], [159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8], [170.2, 72.8], [174.0, 54.5], [173.0, 59.8], [179.9, 67.3], [170.5, 67.8], [160.0, 47.0], [154.4, 46.2], [162.0, 55.0], [176.5, 83.0], [160.0, 54.4], [152.0, 45.8], [162.1, 53.6], [170.0, 73.2], [160.2, 52.1], [161.3, 67.9], [166.4, 56.6], [168.9, 62.3], [163.8, 58.5], [167.6, 54.5], [160.0, 50.2], [161.3, 60.3], [167.6, 58.3], [165.1, 56.2], [160.0, 50.2], [170.0, 72.9], [157.5, 59.8], [167.6, 61.0], [160.7, 69.1], [163.2, 55.9], [152.4, 46.5], [157.5, 54.3], [168.3, 54.8], [180.3, 60.7], [165.5, 60.0], [165.0, 62.0], [164.5, 60.3], [156.0, 52.7], [160.0, 74.3], [163.0, 62.0], [165.7, 73.1], [161.0, 80.0], [162.0, 54.7], [166.0, 53.2], [174.0, 75.7], [172.7, 61.1], [167.6, 55.7], [151.1, 48.7], [164.5, 52.3], [163.5, 50.0], [152.0, 59.3], [169.0, 62.5], [164.0, 55.7], [161.2, 54.8], [155.0, 45.9], [170.0, 70.6], [176.2, 67.2], [170.0, 69.4], [162.5, 58.2], [170.3, 64.8], [164.1, 71.6], [169.5, 52.8], [163.2, 59.8], [154.5, 49.0], [159.8, 50.0], [173.2, 69.2], [170.0, 55.9], [161.4, 63.4], [169.0, 58.2], [166.2, 58.6], [159.4, 45.7], [162.5, 52.2], [159.0, 48.6], [162.8, 57.8], [159.0, 55.6], [179.8, 66.8], [162.9, 59.4], [161.0, 53.6], [151.1, 73.2], [168.2, 53.4], [168.9, 69.0], [173.2, 58.4], [171.8, 56.2], [178.0, 70.6], [164.3, 59.8], [163.0, 72.0], [168.5, 65.2], [166.8, 56.6], [172.7, 105.2], [163.5, 51.8], [169.4, 63.4], [167.8, 59.0], [159.5, 47.6], [167.6, 63.0], [161.2, 55.2], [160.0, 45.0], [163.2, 54.0], [162.2, 50.2], [161.3, 60.2], [149.5, 44.8], [157.5, 58.8], [163.2, 56.4], [172.7, 62.0], [155.0, 49.2], [156.5, 67.2], [164.0, 53.8], [160.9, 54.4], [162.8, 58.0], [167.0, 59.8], [160.0, 54.8], [160.0, 43.2], [168.9, 60.5], [158.2, 46.4], [156.0, 64.4], [160.0, 48.8], [167.1, 62.2], [158.0, 55.5], [167.6, 57.8], [156.0, 54.6], [162.1, 59.2], [173.4, 52.7], [159.8, 53.2], [170.5, 64.5], [159.2, 51.8], [157.5, 56.0], [161.3, 63.6], [162.6, 63.2], [160.0, 59.5], [168.9, 56.8], [165.1, 64.1], [162.6, 50.0], [165.1, 72.3], [166.4, 55.0], [160.0, 55.9], [152.4, 60.4], [170.2, 69.1], [162.6, 84.5], [170.2, 55.9], [158.8, 55.5], [172.7, 69.5], [167.6, 76.4], [162.6, 61.4], [167.6, 65.9], [156.2, 58.6], [175.2, 66.8], [172.1, 56.6], [162.6, 58.6], [160.0, 55.9], [165.1, 59.1], [182.9, 81.8], [166.4, 70.7], [165.1, 56.8], [177.8, 60.0], [165.1, 58.2], [175.3, 72.7], [154.9, 54.1], [158.8, 49.1], [172.7, 75.9], [168.9, 55.0], [161.3, 57.3], [167.6, 55.0], [165.1, 65.5], [175.3, 65.5], [157.5, 48.6], [163.8, 58.6], [167.6, 63.6], [165.1, 55.2], [165.1, 62.7], [168.9, 56.6], [162.6, 53.9], [164.5, 63.2], [176.5, 73.6], [168.9, 62.0], [175.3, 63.6], [159.4, 53.2], [160.0, 53.4], [170.2, 55.0], [162.6, 70.5], [167.6, 54.5], [162.6, 54.5], [160.7, 55.9], [160.0, 59.0], [157.5, 63.6], [162.6, 54.5], [152.4, 47.3], [170.2, 67.7], [165.1, 80.9], [172.7, 70.5], [165.1, 60.9], [170.2, 63.6], [170.2, 54.5], [170.2, 59.1], [161.3, 70.5], [167.6, 52.7], [167.6, 62.7], [165.1, 86.3], [162.6, 66.4], [152.4, 67.3], [168.9, 63.0], [170.2, 73.6], [175.2, 62.3], [175.2, 57.7], [160.0, 55.4], [165.1, 104.1], [174.0, 55.5], [170.2, 77.3], [160.0, 80.5], [167.6, 64.5], [167.6, 72.3], [167.6, 61.4], [154.9, 58.2], [162.6, 81.8], [175.3, 63.6], [171.4, 53.4], [157.5, 54.5], [165.1, 53.6], [160.0, 60.0], [174.0, 73.6], [162.6, 61.4], [174.0, 55.5], [162.6, 63.6], [161.3, 60.9], [156.2, 60.0], [149.9, 46.8], [169.5, 57.3], [160.0, 64.1], [175.3, 63.6], [169.5, 67.3], [160.0, 75.5], [172.7, 68.2], [162.6, 61.4], [157.5, 76.8], [176.5, 71.8], [164.4, 55.5], [160.7, 48.6], [174.0, 66.4], [163.8, 67.3])
        return self._scatterFemaleData

    def getScatterMalePoints(self, series):
        if self._scatterMaleData is not None:
            return self._scatterMaleData
        self._scatterMaleData = self.getPoints(series, [174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8], [181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6], [180.0, 76.6], [177.8, 83.6], [192.0, 90.0], [176.0, 74.6], [174.0, 71.0], [184.0, 79.6], [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9], [176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4], [173.5, 81.8], [178.0, 89.6], [180.3, 82.8], [180.3, 76.4], [164.5, 63.2], [173.0, 60.9], [183.5, 74.8], [175.5, 70.0], [188.0, 72.4], [189.2, 84.1], [172.8, 69.1], [170.0, 59.5], [182.0, 67.2], [170.0, 61.3], [177.8, 68.6], [184.2, 80.1], [186.7, 87.8], [171.4, 84.7], [172.7, 73.4], [175.3, 72.1], [180.3, 82.6], [182.9, 88.7], [188.0, 84.1], [177.2, 94.1], [172.1, 74.9], [167.0, 59.1], [169.5, 75.6], [174.0, 86.2], [172.7, 75.3], [182.2, 87.1], [164.1, 55.2], [163.0, 57.0], [171.5, 61.4], [184.2, 76.8], [174.0, 86.8], [174.0, 72.2], [177.0, 71.6], [186.0, 84.8], [167.0, 68.2], [171.8, 66.1], [182.0, 72.0], [167.0, 64.6], [177.8, 74.8], [164.5, 70.0], [192.0, 101.6], [175.5, 63.2], [171.2, 79.1], [181.6, 78.9], [167.4, 67.7], [181.1, 66.0], [177.0, 68.2], [174.5, 63.9], [177.5, 72.0], [170.5, 56.8], [182.4, 74.5], [197.1, 90.9], [180.1, 93.0], [175.5, 80.9], [180.6, 72.7], [184.4, 68.0], [175.5, 70.9], [180.6, 72.5], [177.0, 72.5], [177.1, 83.4], [181.6, 75.5], [176.5, 73.0], [175.0, 70.2], [174.0, 73.4], [165.1, 70.5], [177.0, 68.9], [192.0, 102.3], [176.5, 68.4], [169.4, 65.9], [182.1, 75.7], [179.8, 84.5], [175.3, 87.7], [184.9, 86.4], [177.3, 73.2], [167.4, 53.9], [178.1, 72.0], [168.9, 55.5], [157.2, 58.4], [180.3, 83.2], [170.2, 72.7], [177.8, 64.1], [172.7, 72.3], [165.1, 65.0], [186.7, 86.4], [165.1, 65.0], [174.0, 88.6], [175.3, 84.1], [185.4, 66.8], [177.8, 75.5], [180.3, 93.2], [180.3, 82.7], [177.8, 58.0], [177.8, 79.5], [177.8, 78.6], [177.8, 71.8], [177.8, 116.4], [163.8, 72.2], [188.0, 83.6], [198.1, 85.5], [175.3, 90.9], [166.4, 85.9], [190.5, 89.1], [166.4, 75.0], [177.8, 77.7], [179.7, 86.4], [172.7, 90.9], [190.5, 73.6], [185.4, 76.4], [168.9, 69.1], [167.6, 84.5], [175.3, 64.5], [170.2, 69.1], [190.5, 108.6], [177.8, 86.4], [190.5, 80.9], [177.8, 87.7], [184.2, 94.5], [176.5, 80.2], [177.8, 72.0], [180.3, 71.4], [171.4, 72.7], [172.7, 84.1], [172.7, 76.8], [177.8, 63.6], [177.8, 80.9], [182.9, 80.9], [170.2, 85.5], [167.6, 68.6], [175.3, 67.7], [165.1, 66.4], [185.4, 102.3], [181.6, 70.5], [172.7, 95.9], [190.5, 84.1], [179.1, 87.3], [175.3, 71.8], [170.2, 65.9], [193.0, 95.9], [171.4, 91.4], [177.8, 81.8], [177.8, 96.8], [167.6, 69.1], [167.6, 82.7], [180.3, 75.5], [182.9, 79.5], [176.5, 73.6], [186.7, 91.8], [188.0, 84.1], [188.0, 85.9], [177.8, 81.8], [174.0, 82.5], [177.8, 80.5], [171.4, 70.0], [185.4, 81.8], [185.4, 84.1], [188.0, 90.5], [188.0, 91.4], [182.9, 89.1], [176.5, 85.0], [175.3, 69.1], [175.3, 73.6], [188.0, 80.5], [188.0, 82.7], [175.3, 86.4], [170.5, 67.7], [179.1, 92.7], [177.8, 93.6], [175.3, 70.9], [182.9, 75.0], [170.8, 93.2], [188.0, 93.2], [180.3, 77.7], [177.8, 61.4], [185.4, 94.1], [168.9, 75.0], [185.4, 83.6], [180.3, 85.5], [174.0, 73.9], [167.6, 66.8], [182.9, 87.3], [160.0, 72.3], [180.3, 88.6], [167.6, 75.5], [186.7, 101.4], [175.3, 91.1], [175.3, 67.3], [175.9, 77.7], [175.3, 81.8], [179.1, 75.5], [181.6, 84.5], [177.8, 76.6], [182.9, 85.0], [177.8, 102.5], [184.2, 77.3], [179.1, 71.8], [176.5, 87.9], [188.0, 94.3], [174.0, 70.9], [167.6, 64.5], [170.2, 77.3], [167.6, 72.3], [188.0, 87.3], [174.0, 80.0], [176.5, 82.3], [180.3, 73.6], [167.6, 74.1], [188.0, 85.9], [180.3, 73.2], [167.6, 76.3], [183.0, 65.9], [183.0, 90.9], [179.1, 89.1], [170.2, 62.3], [177.8, 82.7], [179.1, 79.1], [190.5, 98.2], [177.8, 84.1], [180.3, 83.2], [180.3, 83.2])
        return self._scatterMaleData

    def getDateTimeSeriesPoints(self, series):
        return list([None] * 0)

    def getMasterDetailData(self, series):
        return self.getDateTimePoints(series, 0.8446, 0.8445, 0.8444, 0.8451, 0.8418, 0.8264, 0.8258, 0.8232, 0.8233, 0.8258, 0.8283, 0.8278, 0.8256, 0.8292, 0.8239, 0.8239, 0.8245, 0.8265, 0.8261, 0.8269, 0.8273, 0.8244, 0.8244, 0.8172, 0.8139, 0.8146, 0.8164, 0.82, 0.8269, 0.8269, 0.8269, 0.8258, 0.8247, 0.8286, 0.8289, 0.8316, 0.832, 0.8333, 0.8352, 0.8357, 0.8355, 0.8354, 0.8403, 0.8403, 0.8406, 0.8403, 0.8396, 0.8418, 0.8409, 0.8384, 0.8386, 0.8372, 0.839, 0.84, 0.8389, 0.84, 0.8423, 0.8423, 0.8435, 0.8422, 0.838, 0.8373, 0.8316, 0.8303, 0.8303, 0.8302, 0.8369, 0.84, 0.8385, 0.84, 0.8401, 0.8402, 0.8381, 0.8351, 0.8314, 0.8273, 0.8213, 0.8207, 0.8207, 0.8215, 0.8242, 0.8273, 0.8301, 0.8346, 0.8312, 0.8312, 0.8312, 0.8306, 0.8327, 0.8282, 0.824, 0.8255, 0.8256, 0.8273, 0.8209, 0.8151, 0.8149, 0.8213, 0.8273, 0.8273, 0.8261, 0.8252, 0.824, 0.8262, 0.8258, 0.8261, 0.826, 0.8199, 0.8153, 0.8097, 0.8101, 0.8119, 0.8107, 0.8105, 0.8084, 0.8069, 0.8047, 0.8023, 0.7965, 0.7919, 0.7921, 0.7922, 0.7934, 0.7918, 0.7915, 0.787, 0.7861, 0.7861, 0.7853, 0.7867, 0.7827, 0.7834, 0.7766, 0.7751, 0.7739, 0.7767, 0.7802, 0.7788, 0.7828, 0.7816, 0.7829, 0.783, 0.7829, 0.7781, 0.7811, 0.7831, 0.7826, 0.7855, 0.7855, 0.7845, 0.7798, 0.7777, 0.7822, 0.7785, 0.7744, 0.7743, 0.7726, 0.7766, 0.7806, 0.785, 0.7907, 0.7912, 0.7913, 0.7931, 0.7952, 0.7951, 0.7928, 0.791, 0.7913, 0.7912, 0.7941, 0.7953, 0.7921, 0.7919, 0.7968, 0.7999, 0.7999, 0.7974, 0.7942, 0.796, 0.7969, 0.7862, 0.7821, 0.7821, 0.7821, 0.7811, 0.7833, 0.7849, 0.7819, 0.7809, 0.7809, 0.7827, 0.7848, 0.785, 0.7873, 0.7894, 0.7907, 0.7909, 0.7947, 0.7987, 0.799, 0.7927, 0.79, 0.7878, 0.7878, 0.7907, 0.7922, 0.7937, 0.786, 0.787, 0.7838, 0.7838, 0.7837, 0.7836, 0.7806, 0.7825, 0.7798, 0.777, 0.777, 0.7772, 0.7793, 0.7788, 0.7785, 0.7832, 0.7865, 0.7865, 0.7853, 0.7847, 0.7809, 0.778, 0.7799, 0.78, 0.7801, 0.7765, 0.7785, 0.7811, 0.782, 0.7835, 0.7845, 0.7844, 0.782, 0.7811, 0.7795, 0.7794, 0.7806, 0.7794, 0.7794, 0.7778, 0.7793, 0.7808, 0.7824, 0.787, 0.7894, 0.7893, 0.7882, 0.7871, 0.7882, 0.7871, 0.7878, 0.79, 0.7901, 0.7898, 0.7879, 0.7886, 0.7858, 0.7814, 0.7825, 0.7826, 0.7826, 0.786, 0.7878, 0.7868, 0.7883, 0.7893, 0.7892, 0.7876, 0.785, 0.787, 0.7873, 0.7901, 0.7936, 0.7939, 0.7938, 0.7956, 0.7975, 0.7978, 0.7972, 0.7995, 0.7995, 0.7994, 0.7976, 0.7977, 0.796, 0.7922, 0.7928, 0.7929, 0.7948, 0.797, 0.7953, 0.7907, 0.7872, 0.7852, 0.7852, 0.786, 0.7862, 0.7836, 0.7837, 0.784, 0.7867, 0.7867, 0.7869, 0.7837, 0.7827, 0.7825, 0.7779, 0.7791, 0.779, 0.7787, 0.78, 0.7807, 0.7803, 0.7817, 0.7799, 0.7799, 0.7795, 0.7801, 0.7765, 0.7725, 0.7683, 0.7641, 0.7639, 0.7616, 0.7608, 0.759, 0.7582, 0.7539, 0.75, 0.75, 0.7507, 0.7505, 0.7516, 0.7522, 0.7531, 0.7577, 0.7577, 0.7582, 0.755, 0.7542, 0.7576, 0.7616, 0.7648, 0.7648, 0.7641, 0.7614, 0.757, 0.7587, 0.7588, 0.762, 0.762, 0.7617, 0.7618, 0.7615, 0.7612, 0.7596, 0.758, 0.758, 0.758, 0.7547, 0.7549, 0.7613, 0.7655, 0.7693, 0.7694, 0.7688, 0.7678, 0.7708, 0.7727, 0.7749, 0.7741, 0.7741, 0.7732, 0.7727, 0.7737, 0.7724, 0.7712, 0.772, 0.7721, 0.7717, 0.7704, 0.769, 0.7711, 0.774, 0.7745, 0.7745, 0.774, 0.7716, 0.7713, 0.7678, 0.7688, 0.7718, 0.7718, 0.7728, 0.7729, 0.7698, 0.7685, 0.7681, 0.769, 0.769, 0.7698, 0.7699, 0.7651, 0.7613, 0.7616, 0.7614, 0.7614, 0.7607, 0.7602, 0.7611, 0.7622, 0.7615, 0.7598, 0.7598, 0.7592, 0.7573, 0.7566, 0.7567, 0.7591, 0.7582, 0.7585, 0.7613, 0.7631, 0.7615, 0.76, 0.7613, 0.7627, 0.7627, 0.7608, 0.7583, 0.7575, 0.7562, 0.752, 0.7512, 0.7512, 0.7517, 0.752, 0.7511, 0.748, 0.7509, 0.7531, 0.7531, 0.7527, 0.7498, 0.7493, 0.7504, 0.75, 0.7491, 0.7491, 0.7485, 0.7484, 0.7492, 0.7471, 0.7459, 0.7477, 0.7477, 0.7483, 0.7458, 0.7448, 0.743, 0.7399, 0.7395, 0.7395, 0.7378, 0.7382, 0.7362, 0.7355, 0.7348, 0.7361, 0.7361, 0.7365, 0.7362, 0.7331, 0.7339, 0.7344, 0.7327, 0.7327, 0.7336, 0.7333, 0.7359, 0.7359, 0.7372, 0.736, 0.736, 0.735, 0.7365, 0.7384, 0.7395, 0.7413, 0.7397, 0.7396, 0.7385, 0.7378, 0.7366, 0.74, 0.7411, 0.7406, 0.7405, 0.7414, 0.7431, 0.7431, 0.7438, 0.7443, 0.7443, 0.7443, 0.7434, 0.7429, 0.7442, 0.744, 0.7439, 0.7437, 0.7437, 0.7429, 0.7403, 0.7399, 0.7418, 0.7468, 0.748, 0.748, 0.749, 0.7494, 0.7522, 0.7515, 0.7502, 0.7472, 0.7472, 0.7462, 0.7455, 0.7449, 0.7467, 0.7458, 0.7427, 0.7427, 0.743, 0.7429, 0.744, 0.743, 0.7422, 0.7388, 0.7388, 0.7369, 0.7345, 0.7345, 0.7345, 0.7352, 0.7341, 0.7341, 0.734, 0.7324, 0.7272, 0.7264, 0.7255, 0.7258, 0.7258, 0.7256, 0.7257, 0.7247, 0.7243, 0.7244, 0.7235, 0.7235, 0.7235, 0.7235, 0.7262, 0.7288, 0.7301, 0.7337, 0.7337, 0.7324, 0.7297, 0.7317, 0.7315, 0.7288, 0.7263, 0.7263, 0.7242, 0.7253, 0.7264, 0.727, 0.7312, 0.7305, 0.7305, 0.7318, 0.7358, 0.7409, 0.7454, 0.7437, 0.7424, 0.7424, 0.7415, 0.7419, 0.7414, 0.7377, 0.7355, 0.7315, 0.7315, 0.732, 0.7332, 0.7346, 0.7328, 0.7323, 0.734, 0.734, 0.7336, 0.7351, 0.7346, 0.7321, 0.7294, 0.7266, 0.7266, 0.7254, 0.7242, 0.7213, 0.7197, 0.7209, 0.721, 0.721, 0.721, 0.7209, 0.7159, 0.7133, 0.7105, 0.7099, 0.7099, 0.7093, 0.7093, 0.7076, 0.707, 0.7049, 0.7012, 0.7011, 0.7019, 0.7046, 0.7063, 0.7089, 0.7077, 0.7077, 0.7077, 0.7091, 0.7118, 0.7079, 0.7053, 0.705, 0.7055, 0.7055, 0.7045, 0.7051, 0.7051, 0.7017, 0.7, 0.6995, 0.6994, 0.7014, 0.7036, 0.7021, 0.7002, 0.6967, 0.695, 0.695, 0.6939, 0.694, 0.6922, 0.6919, 0.6914, 0.6894, 0.6891, 0.6904, 0.689, 0.6834, 0.6823, 0.6807, 0.6815, 0.6815, 0.6847, 0.6859, 0.6822, 0.6827, 0.6837, 0.6823, 0.6822, 0.6822, 0.6792, 0.6746, 0.6735, 0.6731, 0.6742, 0.6744, 0.6739, 0.6731, 0.6761, 0.6761, 0.6785, 0.6818, 0.6836, 0.6823, 0.6805, 0.6793, 0.6849, 0.6833, 0.6825, 0.6825, 0.6816, 0.6799, 0.6813, 0.6809, 0.6868, 0.6933, 0.6933, 0.6945, 0.6944, 0.6946, 0.6964, 0.6965, 0.6956, 0.6956, 0.695, 0.6948, 0.6928, 0.6887, 0.6824, 0.6794, 0.6794, 0.6803, 0.6855, 0.6824, 0.6791, 0.6783, 0.6785, 0.6785, 0.6797, 0.68, 0.6803, 0.6805, 0.676, 0.677, 0.677, 0.6736, 0.6726, 0.6764, 0.6821, 0.6831, 0.6842, 0.6842, 0.6887, 0.6903, 0.6848, 0.6824, 0.6788, 0.6814, 0.6814, 0.6797, 0.6769, 0.6765, 0.6733, 0.6729, 0.6758, 0.6758, 0.675, 0.678, 0.6833, 0.6856, 0.6903, 0.6896, 0.6896, 0.6882, 0.6879, 0.6862, 0.6852, 0.6823, 0.6813, 0.6813, 0.6822, 0.6802, 0.6802, 0.6784, 0.6748, 0.6747, 0.6747, 0.6748, 0.6733, 0.665, 0.6611, 0.6583, 0.659, 0.659, 0.6581, 0.6578, 0.6574, 0.6532, 0.6502, 0.6514, 0.6514, 0.6507, 0.651, 0.6489, 0.6424, 0.6406, 0.6382, 0.6382, 0.6341, 0.6344, 0.6378, 0.6439, 0.6478, 0.6481, 0.6481, 0.6494, 0.6438, 0.6377, 0.6329, 0.6336, 0.6333, 0.6333, 0.633, 0.6371, 0.6403, 0.6396, 0.6364, 0.6356, 0.6356, 0.6368, 0.6357, 0.6354, 0.632, 0.6332, 0.6328, 0.6331, 0.6342, 0.6321, 0.6302, 0.6278, 0.6308, 0.6324, 0.6324, 0.6307, 0.6277, 0.6269, 0.6335, 0.6392, 0.64, 0.6401, 0.6396, 0.6407, 0.6423, 0.6429, 0.6472, 0.6485, 0.6486, 0.6467, 0.6444, 0.6467, 0.6509, 0.6478, 0.6461, 0.6461, 0.6468, 0.6449, 0.647, 0.6461, 0.6452, 0.6422, 0.6422, 0.6425, 0.6414, 0.6366, 0.6346, 0.635, 0.6346, 0.6346, 0.6343, 0.6346, 0.6379, 0.6416, 0.6442, 0.6431, 0.6431, 0.6435, 0.644, 0.6473, 0.6469, 0.6386, 0.6356, 0.634, 0.6346, 0.643, 0.6452, 0.6467, 0.6506, 0.6504, 0.6503, 0.6481, 0.6451, 0.645, 0.6441, 0.6414, 0.6409, 0.6409, 0.6428, 0.6431, 0.6418, 0.6371, 0.6349, 0.6333, 0.6334, 0.6338, 0.6342, 0.632, 0.6318, 0.637, 0.6368, 0.6368, 0.6383, 0.6371, 0.6371, 0.6355, 0.632, 0.6277, 0.6276, 0.6291, 0.6274, 0.6293, 0.6311, 0.631, 0.6312, 0.6312, 0.6304, 0.6294, 0.6348, 0.6378, 0.6368, 0.6368, 0.6368, 0.636, 0.637, 0.6418, 0.6411, 0.6435, 0.6427, 0.6427, 0.6419, 0.6446, 0.6468, 0.6487, 0.6594, 0.6666, 0.6666, 0.6678, 0.6712, 0.6705, 0.6718, 0.6784, 0.6811, 0.6811, 0.6794, 0.6804, 0.6781, 0.6756, 0.6735, 0.6763, 0.6762, 0.6777, 0.6815, 0.6802, 0.678, 0.6796, 0.6817, 0.6817, 0.6832, 0.6877, 0.6912, 0.6914, 0.7009, 0.7012, 0.701, 0.7005, 0.7076, 0.7087, 0.717, 0.7105, 0.7031, 0.7029, 0.7006, 0.7035, 0.7045, 0.6956, 0.6988, 0.6915, 0.6914, 0.6859, 0.6778, 0.6815, 0.6815, 0.6843, 0.6846, 0.6846, 0.6923, 0.6997, 0.7098, 0.7188, 0.7232, 0.7262, 0.7266, 0.7359, 0.7368, 0.7337, 0.7317, 0.7387, 0.7467, 0.7461, 0.7366, 0.7319, 0.7361, 0.7437, 0.7432, 0.7461, 0.7461, 0.7454, 0.7549, 0.7742, 0.7801, 0.7903, 0.7876, 0.7928, 0.7991, 0.8007, 0.7823, 0.7661, 0.785, 0.7863, 0.7862, 0.7821, 0.7858, 0.7731, 0.7779, 0.7844, 0.7866, 0.7864, 0.7788, 0.7875, 0.7971, 0.8004, 0.7857, 0.7932, 0.7938, 0.7927, 0.7918, 0.7919, 0.7989, 0.7988, 0.7949, 0.7948, 0.7882, 0.7745, 0.771, 0.775, 0.7791, 0.7882, 0.7882, 0.7899, 0.7905, 0.7889, 0.7879, 0.7855, 0.7866, 0.7865, 0.7795, 0.7758, 0.7717, 0.761, 0.7497, 0.7471, 0.7473, 0.7407, 0.7288, 0.7074, 0.6927, 0.7083, 0.7191, 0.719, 0.7153, 0.7156, 0.7158, 0.714, 0.7119, 0.7129, 0.7129, 0.7049, 0.7095)