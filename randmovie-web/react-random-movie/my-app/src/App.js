import './App.css';
import Button from '@mui/material/Button';
/* import ButtonGroup from '@mui/material/ButtonGroup'; */
import SplitButton from './componentes/SplitButton/'
import RowRadioButtonsGroup from './componentes/RowRadioButtonsGroup'


function App(Componentes) {
  return (
    <>
      <div class="container-full">
        <div class="container-primary">
        {/* <div class="opcoes-radio"><RowRadioButtonsGroup/></div> */}
          <div>
            <p><u>Random movie</u></p>
          </div>
          <div class="btn-principal">
            <Button id="btn-principal" variant="contained" color="error" size="large" fullWidth="true" ><b>Generate</b></Button>
          </div>
          {/* <div class="btn-secundary">
            <Button id="btn-secundary" variant="outlined" color="error"><b>Rate</b></Button>
            <Button id="btn-secundary" variant="outlined" color="error"><b>Gender</b></Button>
            <Button id="btn-secundary" variant="outlined" color="error"><b>Rate and Gender</b></Button>
          </div> */}
          <div class="btn-secundary">
            <Button id="btn-secundary" variant="outlined" color="error" ><b>Rate</b></Button>
            <Button id="btn-secundary" variant="outlined" color="error" ><b>Gender</b></Button>
            <Button id="btn-secundary" variant="outlined" color="error" ><b>Rate and Gender</b></Button>
          </div>
          <div class="fundo-preto"></div>
        </div>
      </div>
    </>
  );
}

export default App;
