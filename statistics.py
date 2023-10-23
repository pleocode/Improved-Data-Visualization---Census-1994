import pandas as pd
from db import read_file



# Groups the data by age
def age_group():
    df = pd.DataFrame(read_file())
    age_group = df.groupby("age")["fnlwgt"].sum().reset_index()
    return age_group

# Calculates the average age
def age_mean():
    age_mean = ((age_group()["age"] * age_group()["fnlwgt"]).sum()) / age_group()["fnlwgt"].sum()
    return age_mean

# Calculates the median of age
def age_median():
    df = age_group()

    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = df["fnlwgt"].cumsum()

    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = df["fnlwgt"].sum()

    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    age_median = df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    return(age_median)

# Calculates the mode of age
def age_mode():
    age_mode = age_group()["age"].iloc[age_group()["fnlwgt"].idxmax()]
    return age_mode

# Groups the data by country
def native_group():
    df = pd.DataFrame(read_file())
    native_group = df.groupby("native.country")["fnlwgt"].sum().reset_index()
    return native_group

# Groups the data by education level
def education_group():
    df = pd.DataFrame(read_file())
    education_group = df.groupby("education.num")["fnlwgt"].sum().reset_index()
    return education_group



#-----------------------Gender Groups-----------------------
# Groups the data by gender
def sex_group():
    df = pd.DataFrame(read_file())
    sex_group = df.groupby("sex")["fnlwgt"].sum().reset_index()
    sex_group = sex_group.sort_values(by="fnlwgt", ascending=False)
    return sex_group

# Groups the data by gender and income
def sex_income_group():
    df = pd.DataFrame(read_file())
    sex_income_group = df.groupby(["sex", "income"])["fnlwgt"].sum().reset_index()
    sex_income_group = sex_income_group.sort_values(by="fnlwgt", ascending=False)
    return sex_income_group

# Groups the data by gender and race
def sex_race_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    sex_race_group = df.groupby(["sex", "race"])["fnlwgt"].sum().reset_index()
    sex_race_group = sex_race_group.sort_values(by="fnlwgt", ascending=False)
    return sex_race_group

# Groups the data by gender and age
def sex_age_group():
    df = pd.DataFrame(read_file())
    sex_age_group = df.groupby(["sex", "age"])["fnlwgt"].sum().reset_index()
    sex_age_group = sex_age_group.sort_values(by="fnlwgt", ascending=False)
    return sex_age_group

# Calculates the age mean per gender
def sex_age_mean():
    df = pd.DataFrame(read_file())
    sex_age_group = df.groupby(["sex", "age"])["fnlwgt"].sum().reset_index()

    # ---------Male
    male_df = sex_age_group[sex_age_group["sex"] == "Male"]
    male_mean = ((male_df["age"]*male_df["fnlwgt"]).sum()) / male_df["fnlwgt"].sum()

    # ---------Female
    female_df = sex_age_group[sex_age_group["sex"] == "Female"]
    female_mean = ((female_df["age"]*female_df["fnlwgt"]).sum()) / female_df["fnlwgt"].sum()

    # ---------Both
    mean = {"Male": "" , "Female": ""}
    mean["Male"] = male_mean
    mean["Female"] = female_mean
    return mean

# Calculates the age median per gender
def sex_age_median():
    df = pd.DataFrame(read_file())
    sex_age_group = df.groupby(["sex", "age"])["fnlwgt"].sum().reset_index()

    # ---------Male
    male_df = sex_age_group[sex_age_group["sex"] == "Male"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = male_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = male_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    male_median = male_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------Female
    female_df = sex_age_group[sex_age_group["sex"] == "Female"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = female_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = female_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    female_median = female_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------Both
    median = {"Male": "", "Female": ""}
    median["Male"] = male_median
    median["Female"] = female_median
    return median

# Calculates the age mode per gender
def sex_age_mode():
    df = pd.DataFrame(read_file())
    sex_age_group = df.groupby(["sex", "age"])["fnlwgt"].sum().reset_index()

    # ---------Male
    male_df = sex_age_group[sex_age_group["sex"] == "Male"].reset_index()
    male_mode = male_df["age"].iloc[male_df["fnlwgt"].idxmax()]

    # ---------Female
    female_df = sex_age_group[sex_age_group["sex"] == "Female"].reset_index()
    female_mode = female_df["age"].iloc[female_df["fnlwgt"].idxmax()]

    # ---------Both
    mode = {"Male": "", "Female": ""}
    mode["Male"] = male_mode
    mode["Female"] = female_mode
    return mode

# Groups the data by gender and education level
def sex_education_group():
    df = pd.DataFrame(read_file())
    sex_education_group = df.groupby(["sex", "education.num"])["fnlwgt"].sum().reset_index()
    sex_education_group = sex_education_group.sort_values(by="fnlwgt", ascending=False)
    return sex_education_group

#-----------------------Income Groups-----------------------
# Groups the data by income (<50k or >50k)
def income_group():
    df = pd.DataFrame(read_file())
    income_group = df.groupby("income")["fnlwgt"].sum().reset_index()
    return income_group

def income_sex_group():
    df = pd.DataFrame(read_file())
    income_sex_group = df.groupby(["income", "sex"])["fnlwgt"].sum().reset_index()
    income_sex_group = income_sex_group.sort_values(by="fnlwgt", ascending=False)
    return income_sex_group

# Groups the data by income and race
def income_race_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    income_race_group = df.groupby(["income", "race"])["fnlwgt"].sum().reset_index()
    income_race_group = income_race_group.sort_values(by="fnlwgt", ascending=False)
    return income_race_group

# Groups the data by income and age
def income_age_group():
    df = pd.DataFrame(read_file())
    income_age_group = df.groupby(["income", "age"])["fnlwgt"].sum().reset_index()
    return income_age_group

# Calculates the age mean per income
def income_age_mean():
    df = pd.DataFrame(read_file())
    income_age_group = df.groupby(["income", "age"])["fnlwgt"].sum().reset_index()

    # ---------<=50k
    below_df = income_age_group[income_age_group["income"] == "<=50K"]
    below_mean = ((below_df["age"]*below_df["fnlwgt"]).sum()) / below_df["fnlwgt"].sum()

    # --------->50K
    above_df = income_age_group[income_age_group["income"] == ">50K"]
    above_mean = ((above_df["age"]*above_df["fnlwgt"]).sum()) / above_df["fnlwgt"].sum()

    # ---------Both
    mean = {"<=50K": "" , ">50K": ""}
    mean["<=50K"] = below_mean
    mean[">50K"] = above_mean
    return mean

# Calculates the age median per income
def income_age_median():
    df = pd.DataFrame(read_file())
    income_age_group = df.groupby(["income", "age"])["fnlwgt"].sum().reset_index()

    # ---------<=50k
    below_df = income_age_group[income_age_group["income"] == "<=50K"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = below_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = below_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    below_median = below_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # --------->50K
    above_df = income_age_group[income_age_group["income"] == ">50K"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = above_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = above_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    above_median = above_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------Both
    median = {"<=50K": "", ">50K": ""}
    median["<=50K"] = below_median
    median[">50K"] = above_median
    return median

# Calculates the age mode per gender
def income_age_mode():
    df = pd.DataFrame(read_file())
    income_age_group = df.groupby(["income", "age"])["fnlwgt"].sum().reset_index()

    # ---------<=50k
    below_df = income_age_group[income_age_group["income"] == "<=50K"].reset_index()
    below_mode = below_df["age"].iloc[below_df["fnlwgt"].idxmax()]

    # --------->50K
    above_df = income_age_group[income_age_group["income"] == ">50K"].reset_index()
    above_mode = above_df["age"].iloc[above_df["fnlwgt"].idxmax()]

    # ---------Both
    mode = {"<=50K": "", ">50K": ""}
    mode["<=50K"] = below_mode
    mode[">50K"] = above_mode
    return mode

# Groups the data by income and education level
def income_education_group():
    df = pd.DataFrame(read_file())
    income_education_group = df.groupby(["income", "education.num"])["fnlwgt"].sum().reset_index()
    return income_education_group
#-----------------------Race Groups-----------------------
# Groups the data by race
def race_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_group = df.groupby("race")["fnlwgt"].sum().reset_index()
    race_group = race_group.sort_values(by="fnlwgt", ascending=False)
    return race_group

# Groups the data by race and gender
def race_sex_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_sex_group = df.groupby(["race", "sex"])["fnlwgt"].sum().reset_index()
    race_sex_group = race_sex_group.sort_values(by="fnlwgt", ascending=False)
    return race_sex_group

# Groups the data by race and income
def race_income_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_income_group = df.groupby(["race", "income"])["fnlwgt"].sum().reset_index()
    race_income_group = race_income_group.sort_values(by="fnlwgt", ascending=False)
    return race_income_group

# Groups the data by race and age
def race_age_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_age_group = df.groupby(["race", "age"])["fnlwgt"].sum().reset_index()
    pivoted_df = race_age_group.pivot(index="age", columns="race", values="fnlwgt").fillna(0)
    column_order = ["White", "Black", "Other"]
    pivoted_df = pivoted_df[column_order]
    return pivoted_df

# Calculates the age mean per race
def race_age_mean():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_age_group = df.groupby(["race", "age"])["fnlwgt"].sum().reset_index()

    # ---------White
    white_df = race_age_group[race_age_group["race"] == "White"]
    white_mean = ((white_df["age"]*white_df["fnlwgt"]).sum()) / white_df["fnlwgt"].sum()

    # ---------Black
    black_df = race_age_group[race_age_group["race"] == "Black"]
    black_mean = ((black_df["age"]*black_df["fnlwgt"]).sum()) / black_df["fnlwgt"].sum()

    # ---------Other
    other_df = race_age_group[race_age_group["race"] == "Other"]
    other_mean = ((other_df["age"]*other_df["fnlwgt"]).sum()) / other_df["fnlwgt"].sum()

    # ---------all
    mean = {"White": "" , "Black": "", "Other": ""}
    mean["White"] = white_mean
    mean["Black"] = black_mean
    mean["Other"] = other_mean
    return mean

# Calculates the age median per race
def race_age_median():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_age_group = df.groupby(["race", "age"])["fnlwgt"].sum().reset_index()

    # ---------White
    white_df = race_age_group[race_age_group["race"] == "White"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = white_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = white_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    white_median = white_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------Black
    black_df = race_age_group[race_age_group["race"] == "Black"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = black_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = black_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    black_median = black_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------Other
    other_df = race_age_group[race_age_group["race"] == "Other"].reset_index()
    # Calculates the cumulative sum of "fnlwgt"
    fnlwgt_cumsum = other_df["fnlwgt"].cumsum()
    # Calculates the total sum of "fnlwgt"
    fnlwgt_total_sum = other_df["fnlwgt"].sum()
    # Find the age where fnlwgt_cumsum passes the middle of fnlwgt_total_sum
    other_median = other_df["age"].iloc[(fnlwgt_cumsum >= (fnlwgt_total_sum / 2)).idxmax()]

    # ---------all
    median = {"White": "", "Black": "", "Other": ""}
    median["White"] = white_median
    median["Black"] = black_median
    median["Other"] = other_median
    return median

def race_age_mode():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_age_group = df.groupby(["race", "age"])["fnlwgt"].sum().reset_index()

    # ---------Other
    white_df = race_age_group[race_age_group["race"] == "White"].reset_index()
    white_mode = white_df["age"].iloc[white_df["fnlwgt"].idxmax()]

    # ---------Black
    black_df = race_age_group[race_age_group["race"] == "Black"].reset_index()
    black_mode = black_df["age"].iloc[black_df["fnlwgt"].idxmax()]

    # ---------Other
    other_df = race_age_group[race_age_group["race"] == "Other"].reset_index()
    other_mode = black_df["age"].iloc[black_df["fnlwgt"].idxmax()]

    # ---------All
    mode = {"White": "", "Black": "", "Other": ""}
    mode["White"] = white_mode
    mode["Black"] = black_mode
    mode["Other"] = other_mode
    return mode

# Groups the data by race and education level
def race_education_group():
    df = pd.DataFrame(read_file())
    grouping_races = {"Amer-Indian-Eskimo": "Other", "Asian-Pac-Islander": "Other", "Other": "Other"}
    df["race"] = df["race"].replace(grouping_races)
    race_education_group = df.groupby(["race", "education.num"])["fnlwgt"].sum().reset_index()
    pivoted_df = race_education_group.pivot(index="education.num", columns="race", values="fnlwgt").fillna(0)
    column_order = ["White", "Black", "Other"]
    pivoted_df = pivoted_df[column_order]
    return pivoted_df

#-----------------------Age Groups-----------------------
# Groups the data by age and education level
def age_education_group():
    df = pd.DataFrame(read_file())
    age_education_group = df.groupby(["age", "education.num"])["fnlwgt"].sum().reset_index()
    pivoted_df = age_education_group.pivot(index="age", columns="education.num", values="fnlwgt").fillna(0)
    return pivoted_df
