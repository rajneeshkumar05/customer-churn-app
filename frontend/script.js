document.getElementById("churnForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
        gender: document.getElementById("gender").value,
        SeniorCitizen: parseInt(document.getElementById("SeniorCitizen").value),
        Partner: document.getElementById("Partner").value,
        Dependents: document.getElementById("Dependents").value,
        tenure: parseInt(document.getElementById("tenure").value),
        PhoneService: document.getElementById("PhoneService").value,
        InternetService: document.getElementById("InternetService").value,
        Contract: document.getElementById("Contract").value,
        MonthlyCharges: parseFloat(document.getElementById("MonthlyCharges").value),
        TotalCharges: parseFloat(document.getElementById("TotalCharges").value)
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    // 🔥 DEBUG LINE (VERY IMPORTANT)
    console.log("Backend response:", result);

    document.getElementById("result").innerHTML =
        `Prediction: <b>${result.churn_prediction}</b><br>
         Probability: <b>${result.churn_probability}%</b>`;
});
