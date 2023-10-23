import matplotlib.pyplot as plt
import seaborn as sns
from statistics import sex_group,age_group, race_group, education_group, income_group, sex_income_group, sex_race_group, sex_age_group, sex_education_group,income_sex_group, income_race_group,income_age_group, income_education_group, age_education_group, race_sex_group, race_income_group, race_age_group, race_education_group, age_mean, age_mode, age_median, sex_age_mean, sex_age_median, sex_age_mode, income_age_mean, income_age_median, income_age_mode, race_age_mean, race_age_median, race_age_mode


#-----------------------------------Gender Charts-----------------------------------
def gender_chart():
    colors = {
        "Male": "saddlebrown",
        "Female": "darkgoldenrod",
    }
    sns.barplot(x="sex", y="fnlwgt", palette=colors, data = sex_group())

def gender_income_chart():
    colors = {
        "Male": "saddlebrown",
        "Female": "darkgoldenrod",
    }
    sns.barplot(x="income", y="fnlwgt", hue="sex", data =sex_income_group(), palette=colors)

def gender_race_chart():
    colors = {
        "Male": "saddlebrown",
        "Female": "darkgoldenrod",
    }
    sns.barplot(x="race", y="fnlwgt", hue="sex",palette=colors, data=sex_race_group())

def gender_age_chart():
    colors = {
        "Male": "saddlebrown",
        "Female": "darkgoldenrod",
    }
    sns.barplot(x="age", y="fnlwgt", hue="sex", palette=colors, data=sex_age_group())

def gender_education_chart():
    colors = {
        "Male": "saddlebrown",
        "Female": "darkgoldenrod",
    }
    sns.barplot(x="education.num", y="fnlwgt", hue="sex", palette=colors, data=sex_education_group())

#-----------------------------------Income Charts-----------------------------------
def income_chart():
    colors = {
        "<=50K": "darkslategrey",
        ">50K": "teal",
    }
    sns.barplot(x="income", y="fnlwgt", data = income_group(), palette=colors)

def income_gender_chart():
    colors = {
        "<=50K": "darkslategrey",
        ">50K": "teal",
    }
    sns.barplot(x="sex", y="fnlwgt", hue="income", palette=colors, data=income_sex_group())

def income_race_chart():
    colors = {
        "<=50K": "darkslategrey",
        ">50K": "teal",
    }
    sns.barplot(x="race", y="fnlwgt", hue="income", palette=colors, data=income_race_group())

def income_age_chart():
    colors = {
        "<=50K": "darkslategrey",
        ">50K": "teal",
    }
    sns.barplot(x="age", y="fnlwgt", hue="income", palette=colors, data=income_age_group())

def income_education_chart():
    colors = {
        "<=50K": "darkslategrey",
        ">50K": "teal",
    }
    sns.barplot(x="education.num", y="fnlwgt", hue="income", palette=colors, data=income_education_group())

#-----------------------------------Race Charts-----------------------------------
def race_chart():
    colors = {
        "White": "darkgreen",
        "Black": "limegreen",
        "Other": "darkseagreen",
    }
    sns.barplot(x="race", y="fnlwgt", palette=colors, data= race_group())

print(race_group())
def race_gender_chart():
    colors = {
        "White": "darkgreen",
        "Black": "limegreen",
        "Other": "darkseagreen",
    }
    sns.barplot(x="sex", y="fnlwgt", hue="race", palette=colors, data=race_sex_group())

def race_income_chart():
    colors = {
        "White": "darkgreen",
        "Black": "limegreen",
        "Other": "darkseagreen",
    }
    sns.barplot(x="income", y="fnlwgt", hue="race", palette=colors, data=race_income_group())

def race_age_chart(ax):
    colors = {
        "White": "darkgreen",
        "Black": "limegreen",
        "Other": "darkseagreen",
    }
    race_age_group().plot(kind="bar", stacked=True, color=colors, ax=ax)

def race_education_chart(ax):
    colors = {
        "White": "darkgreen",
        "Black": "limegreen",
        "Other": "darkseagreen",
    }
    race_education_group().plot(kind="bar", stacked=True, color=colors, ax=ax)

#-----------------------------------------------------------------------------
def age_chart():
    sns.barplot(x="age", y="fnlwgt", data = age_group(), color="Steelblue")

def education_chart():
    sns.barplot(x="education.num", y="fnlwgt", data = education_group(), color="navy")


def age_education_chart():
    age_education_group().plot(kind="bar", stacked=True, figsize=(16, 9))


#----------------------------------------Figure 1----------------------------------------
def figure_1():
    # Create figure
    fig = plt.figure(figsize=(16,9))

    sns.set(style="darkgrid")
    #-----------------1-----------------
    ax1=fig.add_subplot(3,3,1)
    # Create Bar Plot
    gender_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Gender")
    plt.xticks(fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    # -----------------2-----------------
    ax2 = fig.add_subplot(3,3,2)
    # Create Bar Plot
    income_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Income per Year")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.title("Population Description", fontsize=16, fontweight="bold", y=1.2)
    # -----------------3-----------------
    ax3 = fig.add_subplot(3,3,3)
    # Create Bar Plot
    race_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Ethnicity")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    # -----------------4-----------------
    ax4 = fig.add_subplot(3,1,2)
    # Create Bar Plot
    age_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 200000000)
    # add x and y axis labels
    plt.xlabel("Age")
    plt.xticks(range(0, 73, 3), fontsize=9)
    plt.ylabel("Number of People in hundreds of Millions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.text(61, 180000000, f"Mean = {round(age_mean(),2)} / Median = {round(age_median(),2)} / Mode = {round(age_mode(),2)}", fontsize=9, weight="bold", color="Steelblue")
    # -----------------5-----------------
    ax5 = fig.add_subplot(3, 1, 3)
    # Create Bar Plot
    education_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 2000000000)
    # add x and y axis labels
    plt.xlabel("Education Level")
    plt.xticks(range(16), labels=["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th", "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters", "Prof-school", "Doctorate"], fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)

    plt.tight_layout()
    plt.show()

#----------------------------------------Figure 2----------------------------------------
def figure_2():
    # Create figure
    fig = plt.figure(figsize=(16,9))
    sns.set(style="darkgrid")
    #-----------------1-----------------
    ax1=fig.add_subplot(3,3,1)
    # Create Bar Plot
    gender_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Gender")
    plt.xticks(fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------2-----------------
    ax2 = fig.add_subplot(3,3,2)
    # Create Bar Plot
    gender_income_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Income per Year")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.title("Gender Analysis", fontsize=16, fontweight="bold", y=1.2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=3)
    # -----------------3-----------------
    ax3 = fig.add_subplot(3,3,3)
    # Create Bar Plot
    gender_race_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Ethnicity")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------4-----------------
    ax4 = fig.add_subplot(3,1,2)
    # Create Bar Plot
    gender_age_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 200000000)
    # add x and y axis labels
    plt.xlabel("Age")
    plt.xticks(range(0, 73, 3), fontsize=9)
    plt.ylabel("Number of People in hundreds of Millions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    plt.text(61, 180000000,
             f"Mean = {round(sex_age_mean()['Male'],2)} / Median = {round(sex_age_median()['Male'], 2)} / Mode = {round(sex_age_mode()['Male'], 2)}",
             fontsize=9, weight="bold", color="saddlebrown")
    plt.text(61, 170000000,
             f"Mean = {round(sex_age_mean()['Female'], 2)} / Median = {round(sex_age_median()['Female'], 2)} / Mode = {round(sex_age_mode()['Female'], 2)}",
             fontsize=9, weight="bold", color="Darkgoldenrod")
    # -----------------5-----------------
    ax5 = fig.add_subplot(3, 1, 3)
    # Create Bar Plot
    gender_education_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 2000000000)
    # add x and y axis labels
    plt.xlabel("Education Level")
    plt.xticks(range(16), labels=["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th", "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters", "Prof-school", "Doctorate"], fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)

    plt.tight_layout()
    plt.show()

#----------------------------------------Figure 3----------------------------------------
def figure_3():
    # Create figure
    fig = plt.figure(figsize=(16,9))
    sns.set(style="darkgrid")
    #-----------------1-----------------
    ax1=fig.add_subplot(3,3,1)
    # Create Bar Plot
    income_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Income per year")
    plt.xticks(fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------2-----------------
    ax2 = fig.add_subplot(3,3,2)
    # Create Bar Plot
    income_gender_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Gender")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.title("Income Analysis", fontsize=16, fontweight="bold", y=1.2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=3)
    # -----------------3-----------------
    ax3 = fig.add_subplot(3,3,3)
    # Create Bar Plot
    income_race_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Ethnicity")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------4-----------------
    ax4 = fig.add_subplot(3,1,2)
    # Create Bar Plot
    income_age_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 200000000)
    # add x and y axis labels
    plt.xlabel("Age")
    plt.xticks(range(0, 73, 3), fontsize=9)
    plt.ylabel("Number of People in hundreds of Millions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    plt.text(61, 180000000,
             f"Mean = {round(income_age_mean()['<=50K'],2)} / Median = {round(income_age_median()['<=50K'], 2)} / Mode = {round(income_age_mode()['<=50K'], 2)}",
             fontsize=9, weight="bold", color="Darkslategrey")
    plt.text(61, 170000000,
             f"Mean = {round(income_age_mean()['>50K'], 2)} / Median = {round(income_age_median()['>50K'], 2)} / Mode = {round(income_age_mode()['>50K'], 2)}",
             fontsize=9, weight="bold", color="Teal")
    # -----------------5-----------------
    ax5 = fig.add_subplot(3, 1, 3)
    # Create Bar Plot
    income_education_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 2000000000)
    # add x and y axis labels
    plt.xlabel("Education Level")
    plt.xticks(range(16), labels=["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th", "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters", "Prof-school", "Doctorate"], fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)

    plt.tight_layout()
    plt.show()

#----------------------------------------Figure 4----------------------------------------
def figure_4():
    # Create figure
    fig = plt.figure(figsize=(16,9))
    sns.set(style="darkgrid")
    #-----------------1-----------------
    ax1=fig.add_subplot(3,3,1)
    # Create Bar Plot
    race_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Ethnicity")
    plt.xticks(fontsize=9)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------2-----------------
    ax2 = fig.add_subplot(3,3,2)
    # Create Bar Plot
    race_gender_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Gender")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.title("Ethnicity Analysis", fontsize=16, fontweight="bold", y=1.2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=3)
    # -----------------3-----------------
    ax3 = fig.add_subplot(3,3,3)
    # Create Bar Plot
    race_income_chart()
    # Adjust the maximum value for the y axis
    plt.ylim(0, 6000000000)
    # add x and y axis labels
    plt.xlabel("Income per Year")
    plt.xticks(fontsize=9)
    plt.ylabel("")
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    # -----------------4-----------------
    ax4 = fig.add_subplot(3,1,2)
    # Create Bar Plot
    race_age_chart(ax4)
    # Adjust the maximum value for the y axis
    plt.ylim(0, 200000000)
    # add x and y axis labels
    plt.xlabel("Age")
    plt.xticks(range(0, 73, 3), fontsize=9, rotation=0)
    plt.ylabel("Number of People in hundreds of Millions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)
    plt.text(61, 180000000,
             f"Mean = {round(race_age_mean()['White'],2)} / Median = {round(race_age_median()['White'], 2)} / Mode = {round(race_age_mode()['White'], 2)}",
             fontsize=9, weight="bold", color="Darkgreen")
    plt.text(61, 170000000,
             f"Mean = {round(race_age_mean()['Black'], 2)} / Median = {round(race_age_median()['Black'], 2)} / Mode = {round(race_age_mode()['Black'], 2)}",
             fontsize=9, weight="bold", color="Limegreen")
    plt.text(61, 160000000,
             f"Mean = {round(race_age_mean()['Other'], 2)} / Median = {round(race_age_median()['Other'], 2)} / Mode = {round(race_age_mode()['Other'], 2)}",
             fontsize=9, weight="bold", color="darkseagreen")
    # -----------------5-----------------
    ax5 = fig.add_subplot(3, 1, 3)
    # Create Bar Plot
    race_education_chart(ax5)
    # Adjust the maximum value for the y axis
    plt.ylim(0, 2000000000)
    # add x and y axis labels
    plt.xlabel("Education Level")
    plt.xticks(range(16), labels=["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th", "HS-grad", "Some-college", "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters", "Prof-school", "Doctorate"], fontsize=9, rotation=0)
    plt.ylabel("Number of People in Billions", fontsize=10)
    plt.yticks(fontsize=9)
    plt.legend().set_visible(False)

    plt.tight_layout()
    plt.show()



