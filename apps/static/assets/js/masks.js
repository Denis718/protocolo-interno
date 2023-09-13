const mask = () => {
    const cpfList = document.querySelectorAll('.tdCpf');
    const cnpjList = document.querySelectorAll('.tdCnpj');

    cpfList.forEach(cpf => {
        cpf.textContent = cpf.textContent.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    });

    cnpjList.forEach(cnpj => {
        cnpj.textContent = cnpj.textContent.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
    });
};

window.onload = mask;