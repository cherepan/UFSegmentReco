import FWCore.ParameterSet.Config as cms

RU_ME1A = cms.PSet(

    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),


    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(35),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2_str = cms.double(50.0),
    chi2Max = cms.double(100.0),
    dPhiIntMax = cms.double(0.005),
    dPhiMax = cms.double(0.006),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)
RU_ME1B = cms.PSet(
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),

    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(35),
    chi2_str = cms.double(50.0),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2Max = cms.double(100.0),
    dPhiIntMax = cms.double(0.004),
    dPhiMax = cms.double(0.005),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)
RU_ME12 = cms.PSet(


    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),

    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(35),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2_str = cms.double(50.0),
    chi2Max = cms.double(100.0),
    dPhiIntMax = cms.double(0.003),
    dPhiMax = cms.double(0.004),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)
RU_ME13 = cms.PSet(



    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),

    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(20),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2_str = cms.double(30.0),
    chi2Max = cms.double(60.0),
    dPhiIntMax = cms.double(0.002),
    dPhiMax = cms.double(0.003),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)
RU_MEX1 = cms.PSet(


    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),

    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(60),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2_str = cms.double(80.0),
    chi2Max = cms.double(180.0),
    dPhiIntMax = cms.double(0.005),
    dPhiMax = cms.double(0.007),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)
RU_MEX2 = cms.PSet(


    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripxtalksOffset = cms.double(0.03),
    UseAverageTime = cms.bool(False),
    UseParabolaFit = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCUseCalibrations = cms.bool(True),

    CSCUseStaticPedestals = cms.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
#    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
#    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    readBadChannels = cms.bool(True),
    readBadChambers = cms.bool(True),
    CSCUseTimingCorrections = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(True),
    CSCDebug = cms.untracked.bool(False),
    CSCstripWireDeltaTime = cms.int32(8),
    CSCStripClusterSize = cms.untracked.int32(3),

    doCollisions = cms.bool(True),
    chi2Norm_2D_ = cms.double(35),
    SeedBig = cms.double(0.001500),
    SeedSmall = cms.double(0.000200),
    prePrun = cms.bool(True),
    prePrunLimit = cms.double(3.17),
    NormChi2Cut3D = cms.double(10.0),
    NormChi2Cut2D = cms.double(20.0),
    chi2_str = cms.double(50.0),
    chi2Max = cms.double(100.0),
    dPhiIntMax = cms.double(0.004),
    dPhiMax = cms.double(0.006),
    wideSeg = cms.double(3.0),
    minLayersApart = cms.int32(1),
    dRIntMax = cms.double(2.0),
    dRMax = cms.double(1.5),
    #    a XT asymmetry model parameter
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    #
    #    constant systematics (in cm)
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    #
    #    3 time bins noise (in ADC counts)
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
#    readBadChannels = cms.bool(True)


)


CSCSegAlgoUF = cms.PSet(
    chamber_types = cms.vstring('ME1/a', 
        'ME1/b', 
        'ME1/2', 
        'ME1/3', 
        'ME2/1', 
        'ME2/2', 
        'ME3/1', 
        'ME3/2', 
        'ME4/1',
        'ME4/2'),
    algo_name = cms.string('CSCSegAlgoUF'),
    algo_psets = cms.VPSet(
cms.PSet(
        RU_ME1A
    ), 
cms.PSet(
        RU_ME1B
    ),
cms.PSet(
        RU_ME12
    ),
cms.PSet(
        RU_ME13
    ),
cms.PSet(
        RU_MEX1
    ),
cms.PSet(
        RU_MEX2
    )),
#cms.PSet(
#        cscRecHitDParameters)
#    ),
    parameters_per_chamber_type = cms.vint32(1, 2, 3, 4, 5, 
        6, 5, 6, 5, 6)

)

