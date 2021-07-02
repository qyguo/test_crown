import code_generation.quantities.output as q
import code_generation.quantities.nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for contruction of met related quantities
####################

BuildMetVector = Producer(
    name="BuildMetVector",
    call="lorentzvectors::buildMET({df}, {input}, {output})",
    input=[
        nanoAOD.MET_pt,
        nanoAOD.MET_phi,
    ],
    output=[q.met_p4],
    scopes=["et", "mt", "tt", "em"],
)
MetCov00 = Producer(
    name="MetCov00",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_covXX,
    ],
    output=[q.metcov00],
    scopes=["et", "mt", "tt", "em"],
)
MetCov01 = Producer(
    name="MetCov01",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_covXY,
    ],
    output=[q.metcov01],
    scopes=["et", "mt", "tt", "em"],
)
MetCov10 = Producer(
    name="MetCov10",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_covXY,
    ],
    output=[q.metcov10],
    scopes=["et", "mt", "tt", "em"],
)
MetCov11 = Producer(
    name="MetCov11",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_covYY,
    ],
    output=[q.metcov11],
    scopes=["et", "mt", "tt", "em"],
)
MetSumEt = Producer(
    name="MetSumEt",
    call="basefunctions::rename<float>({df}, {input}, {output})",
    input=[
        nanoAOD.MET_sumEt,
    ],
    output=[q.metSumEt],
    scopes=["et", "mt", "tt", "em"],
)

PropagateLeptonsToMET = Producer(
    name="PropagateLeptonsToMET",
    call="met::propagateLeptonsToMET({df}, {input}, {output}, {propagateLeptons})",
    input=[q.met_p4, q.p4_1_uncorrected, q.p4_2_uncorrected, q.p4_1, q.p4_2],
    output=[q.met_p4_leptoncorrected],
    scopes=["et", "mt", "tt", "em"],
)
PropagateJetsToMET = Producer(
    name="PropagateJetsToMET",
    call="met::propagateJetsToMET({df}, {input}, {output}, {propagateJets}, {min_jetpt_met_propagation})",
    input=[
        q.met_p4_leptoncorrected,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        nanoAOD.Jet_mass,
    ],
    output=[q.met_p4_jetcorrected],
    scopes=["et", "mt", "tt", "em"],
)
MetPt = Producer(
    name="MetPt",
    call="met::metPt({df}, {input}, {output})",
    input=[q.met_p4_jetcorrected],
    output=[q.met],
    scopes=["et", "mt", "tt", "em"],
)

MetPhi = Producer(
    name="MetPhi",
    call="met::metPhi({df}, {input}, {output})",
    input=[q.met_p4_jetcorrected],
    output=[q.metphi],
    scopes=["et", "mt", "tt", "em"],
)

MetCorrections = ProducerGroup(
    name="MetCorrections",
    call=None,
    input=None,
    output=None,
    scopes=["et", "mt", "tt", "em"],
    subproducers=[
        BuildMetVector,
        MetCov00,
        MetCov01,
        MetCov10,
        MetCov11,
        MetSumEt,
        PropagateLeptonsToMET,
        PropagateJetsToMET,
        # RecoilCorrections,
        # METunclustered,
        MetPt,
        MetPhi,
    ],
)
