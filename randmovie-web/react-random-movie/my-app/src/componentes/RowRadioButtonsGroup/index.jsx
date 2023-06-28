import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';

export default function RowRadioButtonsGroup() {

  return (
    <FormControl style={{color:'white'}}>
      <RadioGroup
        row
        aria-labelledby="demo-row-radio-buttons-group-label"
        name="row-radio-buttons-group"
      >
        <FormControlLabel value="opcao1" control={<Radio color='error'/>} label="Rate" />
        <FormControlLabel value="opcao2" control={<Radio color='error'/>} label="Gender" />
        <FormControlLabel value="opcao3" control={<Radio color='error' />} label="Rate and gender" />
        {/* <FormControlLabel
          value="disabled"
          disabled
          control={<Radio />}
          label="other"
        /> */}
      </RadioGroup>
    </FormControl>
  );
}