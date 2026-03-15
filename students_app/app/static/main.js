"use strict";

{
    const tbody = document.getElementById("tbody");

    const idBox = document.getElementById("idBox");
    const nameBox = document.getElementById("nameBox");
    const ageBox = document.getElementById("ageBox");
    const btAdd = document.getElementById("btAdd");
    const btUpdate = document.getElementById("btUpdate");
    const btDelete = document.getElementById("btDelete");

    window.addEventListener("load", getALL);

    btAdd.addEventListener("click", async function () {
        const name = nameBox.value;
        const age = ageBox.value;
        const student = { name, age };

        if (!name || !age) {
            alert("Enter name and age");
            return;
        }

        await axios.post("/students", student);
        await getALL();
    });

    btDelete.addEventListener("click", async function () {
        const id = idBox.value;

        if (!id) {
            alert("Enter ID!");
            return;
        }

        try {
            await axios.delete(`/students/${id}`);
            await getALL();
            idBox.value = "";
        } catch (error) {
            console.error(error);
            alert(error.response?.data?.message || "Delete failed");
        }
    });

    btUpdate.addEventListener("click", async function () {
     const id = idBox.value;
     const name = nameBox.value;
     const age = ageBox.value;

     if (!id || !name || !age) {
        alert("Enter ID, name and age");
     }

     const student = { id, name, age };
        
     try {
        await axios.put("/students", student);
        await getALL();
        
        idBox.value = "";
        nameBox.value = "";
        ageBox.value = "";
     } catch (error) { 
        console.error(error);
        alert(error.response?.data?.message || "Update failed");
     }
        
    });

    async function getALL() {
        let response = await axios.get("/students");
        const students = response.data;
        let content = "";

        for (const s of students) {
            content += `
                <tr>
                    <td>${s.id}</td>
                    <td>${s.name}</td>
                    <td>${s.age}</td>
                </tr>
            `;
        }

        tbody.innerHTML = content;
    }
}