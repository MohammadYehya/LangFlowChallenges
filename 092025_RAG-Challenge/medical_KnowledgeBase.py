from langchain.schema import Document

knowledge_base = [

    # ---------------- SYMPTOMS ----------------
    Document(
        id="symptom-fever",
        page_content="Elevated body temperature above 38°C, often accompanied by chills, sweating, and malaise.",
        metadata={"category": "Symptom", "related_conditions": ["Infection", "Inflammatory disease"], "tags": ["general", "systemic"], "source": "CDC"}
    ),
    Document(
        id="symptom-fatigue",
        page_content="Persistent tiredness or lack of energy not relieved by rest.",
        metadata={"category": "Symptom", "related_conditions": ["Anemia", "Depression", "Diabetes"], "tags": ["general"], "source": "WHO"}
    ),
    Document(
        id="symptom-headache",
        page_content="Pain or discomfort in the head, scalp, or neck region, varying in intensity and duration.",
        metadata={"category": "Symptom", "related_conditions": ["Migraine", "Tension headache"], "tags": ["neurological"], "source": "Mayo Clinic"}
    ),
    Document(
        id="symptom-shortness-of-breath",
        page_content="Difficulty breathing or a feeling of breathlessness, especially during exertion.",
        metadata={"category": "Symptom", "related_conditions": ["Asthma", "Heart failure"], "tags": ["respiratory"], "source": "NHS"}
    ),
    Document(
        id="symptom-chest-pain",
        page_content="Discomfort or pain in the chest area, may radiate to the arm, neck, or jaw.",
        metadata={"category": "Symptom", "related_conditions": ["Heart attack", "Angina", "GERD"], "tags": ["cardiovascular"], "source": "American Heart Association"}
    ),
    Document(
        id="symptom-nausea",
        page_content="A sensation of unease and discomfort in the stomach with an urge to vomit.",
        metadata={"category": "Symptom", "related_conditions": ["Gastritis", "Pregnancy", "Food poisoning"], "tags": ["digestive"], "source": "Cleveland Clinic"}
    ),
    Document(
        id="symptom-vomiting",
        page_content="Forceful expulsion of stomach contents through the mouth.",
        metadata={"category": "Symptom", "related_conditions": ["Food poisoning", "Gastroenteritis"], "tags": ["digestive"], "source": "Mayo Clinic"}
    ),
    Document(
        id="symptom-diarrhea",
        page_content="Frequent loose or watery bowel movements.",
        metadata={"category": "Symptom", "related_conditions": ["Infections", "IBS"], "tags": ["digestive"], "source": "WHO"}
    ),
    Document(
        id="symptom-constipation",
        page_content="Difficulty or infrequent bowel movements, often associated with hard stools.",
        metadata={"category": "Symptom", "related_conditions": ["Dehydration", "IBS"], "tags": ["digestive"], "source": "NHS"}
    ),
    Document(
        id="symptom-weight-loss-unexplained",
        page_content="Unintended weight loss without changes in diet or exercise.",
        metadata={"category": "Symptom", "related_conditions": ["Cancer", "Hyperthyroidism"], "tags": ["general"], "source": "NIH"}
    ),
    Document(
        id="symptom-night-sweats",
        page_content="Excessive sweating during sleep, often soaking clothes or bedding.",
        metadata={"category": "Symptom", "related_conditions": ["Tuberculosis", "Lymphoma"], "tags": ["systemic"], "source": "CDC"}
    ),
    Document(
        id="symptom-dizziness",
        page_content="Lightheadedness or a sensation of spinning.",
        metadata={"category": "Symptom", "related_conditions": ["Vertigo", "Low blood pressure"], "tags": ["neurological"], "source": "Mayo Clinic"}
    ),
    Document(
        id="symptom-palpitations",
        page_content="Awareness of rapid, irregular, or strong heartbeat.",
        metadata={"category": "Symptom", "related_conditions": ["Arrhythmia", "Anxiety"], "tags": ["cardiovascular"], "source": "American Heart Association"}
    ),
    Document(
        id="symptom-swelling-legs",
        page_content="Accumulation of fluid in the lower extremities, causing puffiness or heaviness.",
        metadata={"category": "Symptom", "related_conditions": ["Heart failure", "Kidney disease"], "tags": ["edema"], "source": "NIH"}
    ),
    Document(
        id="symptom-itchy-skin",
        page_content="Persistent itching sensation on the skin, may be localized or generalized.",
        metadata={"category": "Symptom", "related_conditions": ["Eczema", "Allergy"], "tags": ["dermatology"], "source": "DermNet"}
    ),
    Document(
        id="symptom-joint-pain",
        page_content="Discomfort, soreness, or aching in one or more joints.",
        metadata={"category": "Symptom", "related_conditions": ["Arthritis", "Injury"], "tags": ["musculoskeletal"], "source": "Arthritis Foundation"}
    ),
    Document(
        id="symptom-memory-loss",
        page_content="Partial or complete inability to recall recent or past events.",
        metadata={"category": "Symptom", "related_conditions": ["Alzheimer's disease", "Stroke"], "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="symptom-blurred-vision",
        page_content="Loss of sharpness of eyesight, making objects appear hazy.",
        metadata={"category": "Symptom", "related_conditions": ["Diabetes", "Cataract"], "tags": ["ophthalmology"], "source": "American Academy of Ophthalmology"}
    ),
    Document(
        id="symptom-frequent-urination",
        page_content="Need to urinate more often than usual, including at night.",
        metadata={"category": "Symptom", "related_conditions": ["Diabetes", "UTI"], "tags": ["urology"], "source": "Mayo Clinic"}
    ),
    Document(
        id="symptom-loss-of-appetite",
        page_content="Decreased desire to eat, leading to reduced food intake.",
        metadata={"category": "Symptom", "related_conditions": ["Cancer", "Infections"], "tags": ["general"], "source": "NHS"}
    ),
    Document(
        id="symptom-sore-throat",
        page_content="Pain or irritation of the throat, often worsened when swallowing.",
        metadata={"category": "Symptom", "related_conditions": ["Pharyngitis", "Tonsillitis"], "tags": ["respiratory"], "source": "CDC"}
    ),
    Document(
        id="symptom-cough",
        page_content="Sudden expulsion of air from the lungs, often to clear the airway.",
        metadata={"category": "Symptom", "related_conditions": ["Bronchitis", "Pneumonia"], "tags": ["respiratory"], "source": "NHS"}
    ),
    Document(
        id="symptom-anxiety",
        page_content="Excessive worry, nervousness, or fear that interferes with daily life.",
        metadata={"category": "Symptom", "related_conditions": ["Generalized Anxiety Disorder", "PTSD"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="symptom-depressed-mood",
        page_content="Persistent sadness, hopelessness, or loss of interest in usual activities.",
        metadata={"category": "Symptom", "related_conditions": ["Major Depressive Disorder"], "tags": ["mental health"], "source": "NIMH"}
    ),
    Document(
        id="symptom-numbness-limbs",
        page_content="Loss of sensation or tingling in arms or legs.",
        metadata={"category": "Symptom", "related_conditions": ["Stroke", "Neuropathy"], "tags": ["neurological"], "source": "NIH"}
    ),

    # ---------------- DIAGNOSES ----------------
    Document(
        id="diagnosis-hypertension",
        page_content="Hypertension is a chronic condition characterized by elevated blood pressure above 140/90 mmHg.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Headache", "Dizziness"], "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="diagnosis-type1-diabetes",
        page_content="Type 1 Diabetes is an autoimmune condition where the body destroys insulin-producing beta cells in the pancreas.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Excessive thirst", "Frequent urination"], "tags": ["endocrine"], "source": "ADA"}
    ),
    Document(
        id="diagnosis-type2-diabetes",
        page_content="Type 2 Diabetes is a metabolic disorder caused by insulin resistance and relative insulin deficiency.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Fatigue", "Blurred vision"], "tags": ["endocrine"], "source": "ADA"}
    ),
    Document(
        id="diagnosis-asthma",
        page_content="Asthma is a chronic inflammatory airway disease causing episodes of wheezing, shortness of breath, and cough.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Wheezing", "Cough"], "tags": ["respiratory"], "source": "GINA"}
    ),
    Document(
        id="diagnosis-copd",
        page_content="Chronic Obstructive Pulmonary Disease (COPD) is a progressive lung disease characterized by airflow limitation.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Chronic cough", "Dyspnea"], "tags": ["respiratory"], "source": "WHO"}
    ),
    Document(
        id="diagnosis-tuberculosis",
        page_content="Tuberculosis is an infectious disease caused by Mycobacterium tuberculosis, primarily affecting the lungs.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Cough", "Night sweats"], "tags": ["infectious"], "source": "CDC"}
    ),
    Document(
        id="diagnosis-influenza",
        page_content="Influenza is a viral respiratory infection characterized by fever, chills, cough, and body aches.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Fever", "Sore throat"], "tags": ["infectious"], "source": "CDC"}
    ),
    Document(
        id="diagnosis-pneumonia",
        page_content="Pneumonia is an infection of the lung tissue caused by bacteria, viruses, or fungi.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Cough", "Chest pain"], "tags": ["infectious"], "source": "WHO"}
    ),
    Document(
        id="diagnosis-coronary-artery-disease",
        page_content="Coronary artery disease occurs when coronary arteries are narrowed or blocked by plaque buildup.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Chest pain", "Palpitations"], "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="diagnosis-heart-failure",
        page_content="Heart failure occurs when the heart cannot pump blood efficiently to meet the body’s needs.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Dyspnea", "Leg swelling"], "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="diagnosis-stroke",
        page_content="Stroke occurs when blood flow to the brain is interrupted, leading to brain damage.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Sudden numbness", "Confusion"], "tags": ["neurological"], "source": "WHO"}
    ),
    Document(
        id="diagnosis-alzheimers",
        page_content="Alzheimer’s disease is a progressive neurodegenerative disorder leading to memory loss and cognitive decline.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Memory loss", "Disorientation"], "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-parkinsons",
        page_content="Parkinson’s disease is a neurodegenerative disorder affecting movement, caused by dopamine deficiency.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Tremor", "Rigidity"], "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-depression",
        page_content="Major Depressive Disorder is a mental health condition characterized by persistent sadness and lack of interest.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Depressed mood", "Fatigue"], "tags": ["mental health"], "source": "NIMH"}
    ),
    Document(
        id="diagnosis-anxiety-disorder",
        page_content="Generalized Anxiety Disorder is excessive, persistent worry difficult to control and interfering with daily life.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Restlessness", "Muscle tension"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="diagnosis-bipolar-disorder",
        page_content="Bipolar disorder is a mental illness marked by extreme shifts in mood, energy, and activity levels.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Mania", "Depression"], "tags": ["mental health"], "source": "NIMH"}
    ),
    Document(
        id="diagnosis-ptsd",
        page_content="Post-traumatic stress disorder occurs after experiencing or witnessing traumatic events.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Flashbacks", "Anxiety"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="diagnosis-osteoporosis",
        page_content="Osteoporosis is a bone disease causing weakened bones and increased fracture risk.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Back pain", "Bone fractures"], "tags": ["musculoskeletal"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-rheumatoid-arthritis",
        page_content="Rheumatoid arthritis is an autoimmune disorder causing joint inflammation and damage.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Joint pain", "Stiffness"], "tags": ["musculoskeletal"], "source": "Arthritis Foundation"}
    ),
    Document(
        id="diagnosis-lung-cancer",
        page_content="Lung cancer is the uncontrolled growth of abnormal cells in the lung tissue.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Persistent cough", "Weight loss"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-breast-cancer",
        page_content="Breast cancer originates in breast tissue, often detected via lump or mammogram.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Breast lump", "Skin changes"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-colorectal-cancer",
        page_content="Colorectal cancer develops in the colon or rectum, often detected through screening.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Rectal bleeding", "Weight loss"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-prostate-cancer",
        page_content="Prostate cancer develops in the prostate gland, common in older men.",
        metadata={"category": "Diagnosis", "common_symptoms": ["Urinary issues", "Pelvic discomfort"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="diagnosis-skin-cancer",
        page_content="Skin cancer arises from abnormal growth of skin cells due to UV radiation.",
        metadata={"category": "Diagnosis", "common_symptoms": ["New mole", "Skin changes"], "tags": ["oncology"], "source": "NIH"}
    ),

    # ---------------- TREATMENTS ----------------
    Document(
        id="treatment-antibiotics",
        page_content="Antibiotics are medications used to treat bacterial infections by killing or inhibiting bacterial growth.",
        metadata={"category": "Treatment", "indicated_for": ["Bacterial infections"], "tags": ["pharmacology"], "source": "CDC"}
    ),
    Document(
        id="treatment-antivirals",
        page_content="Antiviral drugs treat viral infections by inhibiting viral replication.",
        metadata={"category": "Treatment", "indicated_for": ["Influenza", "HIV"], "tags": ["pharmacology"], "source": "CDC"}
    ),
    Document(
        id="treatment-chemotherapy",
        page_content="Chemotherapy uses cytotoxic drugs to kill rapidly dividing cancer cells.",
        metadata={"category": "Treatment", "indicated_for": ["Cancer"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="treatment-radiation-therapy",
        page_content="Radiation therapy uses high-energy radiation to shrink or destroy cancer cells.",
        metadata={"category": "Treatment", "indicated_for": ["Cancer"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="treatment-immunotherapy",
        page_content="Immunotherapy boosts the body's immune system to fight cancer or infections.",
        metadata={"category": "Treatment", "indicated_for": ["Cancer", "Autoimmune diseases"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="treatment-surgery",
        page_content="Surgical procedures involve physically removing diseased tissue or organs.",
        metadata={"category": "Treatment", "indicated_for": ["Cancer", "Appendicitis"], "tags": ["surgical"], "source": "NIH"}
    ),
    Document(
        id="treatment-insulin-therapy",
        page_content="Insulin therapy is the administration of insulin to manage blood glucose in diabetes.",
        metadata={"category": "Treatment", "indicated_for": ["Type 1 Diabetes", "Type 2 Diabetes"], "tags": ["endocrine"], "source": "ADA"}
    ),
    Document(
        id="treatment-antihypertensives",
        page_content="Antihypertensive drugs lower blood pressure through various mechanisms, such as ACE inhibition or beta-blockade.",
        metadata={"category": "Treatment", "indicated_for": ["Hypertension"], "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="treatment-antidepressants",
        page_content="Antidepressant medications help regulate mood in depressive disorders.",
        metadata={"category": "Treatment", "indicated_for": ["Depression", "Anxiety"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="treatment-cbt",
        page_content="Cognitive Behavioral Therapy (CBT) is a structured psychotherapy that modifies dysfunctional thoughts and behaviors.",
        metadata={"category": "Treatment", "indicated_for": ["Depression", "Anxiety"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="treatment-physical-therapy",
        page_content="Physical therapy helps restore movement and strength after injuries or surgeries.",
        metadata={"category": "Treatment", "indicated_for": ["Stroke recovery", "Musculoskeletal injuries"], "tags": ["rehabilitation"], "source": "NIH"}
    ),
    Document(
        id="treatment-vaccination",
        page_content="Vaccination introduces antigens to stimulate immunity and prevent infectious diseases.",
        metadata={"category": "Treatment", "indicated_for": ["Infectious diseases"], "tags": ["preventive"], "source": "CDC"}
    ),
    Document(
        id="treatment-oxygen-therapy",
        page_content="Oxygen therapy supplies supplemental oxygen to patients with respiratory conditions.",
        metadata={"category": "Treatment", "indicated_for": ["COPD", "Pneumonia"], "tags": ["respiratory"], "source": "NHS"}
    ),
    Document(
        id="treatment-dialysis",
        page_content="Dialysis removes waste products and excess fluid from the blood when kidneys fail.",
        metadata={"category": "Treatment", "indicated_for": ["Chronic Kidney Disease"], "tags": ["renal"], "source": "NIH"}
    ),
    Document(
        id="treatment-lifestyle-modification",
        page_content="Lifestyle modifications include diet, exercise, and stress reduction to improve health outcomes.",
        metadata={"category": "Treatment", "indicated_for": ["Hypertension", "Diabetes"], "tags": ["preventive"], "source": "WHO"}
    ),
    Document(
        id="treatment-analgesics",
        page_content="Analgesic medications relieve pain without treating the underlying condition.",
        metadata={"category": "Treatment", "indicated_for": ["Pain"], "tags": ["pain management"], "source": "NIH"}
    ),
    Document(
        id="treatment-antiepileptics",
        page_content="Antiepileptic drugs control seizures by stabilizing neuronal activity.",
        metadata={"category": "Treatment", "indicated_for": ["Epilepsy"], "tags": ["neurology"], "source": "NIH"}
    ),
    Document(
        id="treatment-anticoagulants",
        page_content="Anticoagulant medications prevent blood clot formation and reduce stroke risk.",
        metadata={"category": "Treatment", "indicated_for": ["Atrial fibrillation", "DVT"], "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="treatment-inhalers",
        page_content="Inhalers deliver bronchodilator or corticosteroid medication directly to the lungs.",
        metadata={"category": "Treatment", "indicated_for": ["Asthma", "COPD"], "tags": ["respiratory"], "source": "GINA"}
    ),
    Document(
        id="treatment-antifungals",
        page_content="Antifungal medications treat fungal infections such as candidiasis and ringworm.",
        metadata={"category": "Treatment", "indicated_for": ["Fungal infections"], "tags": ["pharmacology"], "source": "CDC"}
    ),
    Document(
        id="treatment-stem-cell-transplant",
        page_content="Stem cell transplants replace damaged bone marrow with healthy stem cells.",
        metadata={"category": "Treatment", "indicated_for": ["Leukemia", "Lymphoma"], "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="treatment-antipsychotics",
        page_content="Antipsychotic medications treat psychosis, including schizophrenia and bipolar disorder.",
        metadata={"category": "Treatment", "indicated_for": ["Schizophrenia", "Bipolar Disorder"], "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="treatment-hormone-replacement",
        page_content="Hormone replacement therapy supplements deficient hormones, such as estrogen or testosterone.",
        metadata={"category": "Treatment", "indicated_for": ["Menopause", "Hypogonadism"], "tags": ["endocrine"], "source": "NIH"}
    ),
    Document(
        id="treatment-nutrition-therapy",
        page_content="Medical nutrition therapy involves specialized diets for managing chronic diseases.",
        metadata={"category": "Treatment", "indicated_for": ["Diabetes", "Kidney disease"], "tags": ["dietary"], "source": "ADA"}
    ),
    Document(
        id="treatment-gene-therapy",
        page_content="Gene therapy introduces or modifies genetic material to treat inherited diseases.",
        metadata={"category": "Treatment", "indicated_for": ["Genetic disorders"], "tags": ["biotechnology"], "source": "NIH"}
    ),

    # ---------------- OUTCOMES ----------------
    Document(
        id="outcome-hypertension-controlled",
        page_content="Controlled hypertension reduces the risk of heart attack, stroke, and kidney failure.",
        metadata={"category": "Outcome", "condition": "Hypertension", "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="outcome-diabetes-managed",
        page_content="Well-managed diabetes decreases the risk of complications such as neuropathy and retinopathy.",
        metadata={"category": "Outcome", "condition": "Diabetes", "tags": ["endocrine"], "source": "ADA"}
    ),
    Document(
        id="outcome-asthma-managed",
        page_content="Asthma control results in fewer exacerbations, improved lung function, and better quality of life.",
        metadata={"category": "Outcome", "condition": "Asthma", "tags": ["respiratory"], "source": "GINA"}
    ),
    Document(
        id="outcome-cancer-remission",
        page_content="Successful treatment may lead to remission, where cancer is undetectable for years.",
        metadata={"category": "Outcome", "condition": "Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-depression-improved",
        page_content="Depression treatment often results in improved mood, sleep, and daily functioning.",
        metadata={"category": "Outcome", "condition": "Depression", "tags": ["mental health"], "source": "NIMH"}
    ),
    Document(
        id="outcome-anxiety-controlled",
        page_content="Effective treatment reduces excessive worry, panic attacks, and improves social functioning.",
        metadata={"category": "Outcome", "condition": "Anxiety", "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="outcome-heart-failure-managed",
        page_content="Proper therapy can improve symptoms and extend survival, though disease is often progressive.",
        metadata={"category": "Outcome", "condition": "Heart Failure", "tags": ["cardiovascular"], "source": "AHA"}
    ),
    Document(
        id="outcome-stroke-recovery",
        page_content="Stroke recovery varies but rehabilitation can restore mobility, speech, and independence.",
        metadata={"category": "Outcome", "condition": "Stroke", "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="outcome-alzheimers-progression",
        page_content="Alzheimer’s progresses gradually, with worsening memory, behavior, and daily functioning.",
        metadata={"category": "Outcome", "condition": "Alzheimer's Disease", "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="outcome-parkinsons-progression",
        page_content="Parkinson’s disease gradually worsens over time, but medication can improve symptoms.",
        metadata={"category": "Outcome", "condition": "Parkinson's Disease", "tags": ["neurological"], "source": "NIH"}
    ),
    Document(
        id="outcome-copd-progression",
        page_content="COPD is progressive, but early treatment and lifestyle changes can slow decline.",
        metadata={"category": "Outcome", "condition": "COPD", "tags": ["respiratory"], "source": "WHO"}
    ),
    Document(
        id="outcome-osteoporosis-managed",
        page_content="Osteoporosis management reduces fracture risk and improves mobility.",
        metadata={"category": "Outcome", "condition": "Osteoporosis", "tags": ["musculoskeletal"], "source": "NIH"}
    ),
    Document(
        id="outcome-rheumatoid-arthritis-managed",
        page_content="Disease-modifying therapies improve joint health, reduce pain, and slow progression.",
        metadata={"category": "Outcome", "condition": "Rheumatoid Arthritis", "tags": ["musculoskeletal"], "source": "Arthritis Foundation"}
    ),
    Document(
        id="outcome-tuberculosis-treated",
        page_content="With full antibiotic treatment, most tuberculosis cases are cured, though resistance is a risk.",
        metadata={"category": "Outcome", "condition": "Tuberculosis", "tags": ["infectious"], "source": "CDC"}
    ),
    Document(
        id="outcome-influenza-recovered",
        page_content="Most influenza cases resolve within 1–2 weeks, though complications can occur in high-risk groups.",
        metadata={"category": "Outcome", "condition": "Influenza", "tags": ["infectious"], "source": "CDC"}
    ),
    Document(
        id="outcome-pneumonia-recovered",
        page_content="Most patients recover from pneumonia with treatment, but severe cases may cause long-term damage.",
        metadata={"category": "Outcome", "condition": "Pneumonia", "tags": ["infectious"], "source": "WHO"}
    ),
    Document(
        id="outcome-breast-cancer-survival",
        page_content="Breast cancer survival rates are high with early detection and treatment.",
        metadata={"category": "Outcome", "condition": "Breast Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-lung-cancer-prognosis",
        page_content="Lung cancer prognosis varies; survival is better with early-stage diagnosis.",
        metadata={"category": "Outcome", "condition": "Lung Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-colorectal-cancer-survival",
        page_content="Colorectal cancer survival improves significantly with early detection and surgery.",
        metadata={"category": "Outcome", "condition": "Colorectal Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-prostate-cancer-survival",
        page_content="Prostate cancer often has excellent survival rates, particularly when localized.",
        metadata={"category": "Outcome", "condition": "Prostate Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-skin-cancer-survival",
        page_content="Skin cancer has a high survival rate if treated early, but melanoma can be aggressive.",
        metadata={"category": "Outcome", "condition": "Skin Cancer", "tags": ["oncology"], "source": "NIH"}
    ),
    Document(
        id="outcome-ptsd-improvement",
        page_content="With therapy and medication, PTSD symptoms can improve, though some cases remain chronic.",
        metadata={"category": "Outcome", "condition": "PTSD", "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="outcome-bipolar-managed",
        page_content="With mood stabilizers and therapy, many patients with bipolar disorder maintain stable functioning.",
        metadata={"category": "Outcome", "condition": "Bipolar Disorder", "tags": ["mental health"], "source": "NIMH"}
    ),
    Document(
        id="outcome-schizophrenia-managed",
        page_content="Antipsychotic therapy allows many patients with schizophrenia to live functional lives, though relapses are common.",
        metadata={"category": "Outcome", "condition": "Schizophrenia", "tags": ["mental health"], "source": "APA"}
    ),
    Document(
        id="outcome-kidney-disease-managed",
        page_content="Dialysis and transplantation improve survival in chronic kidney disease, though quality of life may be affected.",
        metadata={"category": "Outcome", "condition": "Chronic Kidney Disease", "tags": ["renal"], "source": "NIH"}
    )
]
