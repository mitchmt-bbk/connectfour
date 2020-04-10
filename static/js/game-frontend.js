$(document).ready(() => {

	function main(){

		let canPlayerMakeMove = true,
			tokenWidth = getTokenWidth(),
			tokenNum = 0,
			showRestButton = false,
			resetBtn = $('.reset-btn'),
			playAgainBtn = $('.play-again'),
			overlay = $('.overlay'),
			maxRowNum = 5,
			playerWins = 0,
			aiWins = 0;

		$('.col').on('click',function(){
			
			if (!showRestButton) {
				showRestButton = true;
				resetBtn.fadeIn();
			}

			if (canPlayerMakeMove) {
				let playerMoveCol = $(this).data('column'),
					playerMoveRow = getNextAvailableRow(playerMoveCol),
					playerMove = [playerMoveCol,playerMoveRow];

				// Check if column is full
				if (playerMoveRow > maxRowNum) {
					fullColumnError(playerMoveCol);
					return;
				}

				canPlayerMakeMove = false;
				let tokenData = {
					owner: 'player',
					width: tokenWidth,
					number: tokenNum,
					position: playerMove
				};
				token = createToken(tokenData);
				tokenNum++;
				placeToken(token, playerMove);

				$.ajax({
					data: {
						player_move: playerMoveCol
					},
					type: 'POST',
					url: '/process-move'
				})
				.done(function(data){
					console.log(data);
					if (data.is_win == 1) {
						let popUpContent = [
							'player-win',
							'You won!',
							'Congratulations, you beat the AI!'
						];
						playerWins++;
						updateWinsCounter('player',playerWins);
						displayPopUp(popUpContent);
					} else if (data.is_win == 2) {
						let popUpContent = [
							'player-lose',
							'You lost!',
							'Oh dear, the AI beat you...'
						];
						aiWins++;
						updateWinsCounter('ai',aiWins);
						displayPopUp(popUpContent);
					} else if (data.is_win == 3) {
						let popUpContent = [
							'draw',
							'It was a draw',
							'Close one! Why not try your luck again?'
						];
						displayPopUp(popUpContent);
					} else {
						setTimeout(function(){

							// For demo purposes START
							let aiMoveCol = data.ai_move[0],
								aiMoveRow = getNextAvailableRow(aiMoveCol),
								aiMove = [aiMoveCol,aiMoveRow];

							let tokenData = {
								owner: 'ai',
								width: tokenWidth,
								number: tokenNum,
								position: aiMove
							};

							let token = createToken(tokenData);
							tokenNum++;

							placeToken(token, aiMove);
							// For demo purposes END

							// How it should actually work
							// placeToken(token, data.ai_move);

						}, 750);
						// TODO Leave the below but change to 500ms
						setTimeout(function(){
							canPlayerMakeMove = true;
						}, 1000)
					}
				})
			} else {
				console.log('Wait your turn!');
			}
		});

		checkDeviceOrientation();

		$(window).on('resize orientationchange', function() {
			tokenWidth = getTokenWidth();
			$('.token').css({'width': tokenWidth, 'height': tokenWidth});
			replaceTokens();
			checkDeviceOrientation();
		});

		resetBtn.on('click',function(){
			showRestButton = false;
			canPlayerMakeMove = true;
			resetBtn.fadeOut('fast');
			overlay.fadeOut();
			resetGame();
		});

		playAgainBtn.on('click',function(){
			showRestButton = false;
			canPlayerMakeMove = true;
			resetBtn.fadeOut('fast');
			removePopUp();
			resetGame();
		});

	}

	function updateWinsCounter(winner,wins){
		$('.wins-counter.'+winner).find('h2').text(wins);
	}

	function replaceTokens(){
		let allTokens = $('.token');
		for (var i = 0; i < allTokens.length; i++) {
			let col = $(allTokens[i]).data('col'),
				row = $(allTokens[i]).data('row');
			placeToken($(allTokens[i]), [col,row]);
		}					
	}

	function checkDeviceOrientation(){
		let deviceWidth = $(window).width(),
			deviceHeight = $(window).height()
			minPortraitWidth = 1024;

		if (deviceHeight > deviceWidth && deviceWidth < minPortraitWidth) {
			let popUpContent = [
				'landscape-alert',
				'Landscape, please!',
				'Please change the orientation of your device to be landscape.'
			];
			displayPopUp(popUpContent);
		} else {
			removePopUp();
		}
	}

	function getNextAvailableRow(chosenCol) {
		let col = $(document).find(`.col[data-column='${chosenCol}']`),
			rowCells = $(col[0]).find('.token').length;
		return rowCells;
	}

	function createToken(tokenData) {
		let tokenEl = $('<div></div>')
			.addClass("token "+tokenData.owner+"")
			.css({
				'width': tokenData.width, 
				'height': tokenData.width
			})
			.attr({ 
				'id' : "token-"+tokenData.number+"",
				'data-col': tokenData.position[0],
				'data-row': tokenData.position[1]
			});

		return tokenEl;
	}

	function placeToken(token, tokenPosition){
		let tokenId = $(token).attr('id'),
			rowPos = calcRowPosition(tokenPosition[0],tokenPosition[1]);

		token.prependTo($(document).find(`.col[data-column='${tokenPosition[0]}']`));

		anime({
		  targets: '#'+tokenId,
		  translateY: rowPos,
		  easing: 'easeOutBounce',
		});
	}

	function calcRowPosition(colNum, rowNum){
		let col = $(document).find(`.col[data-column='${colNum}']`),
			rowCell = $(col[0]).find(`.cell-square[data-row='${rowNum}']`),
			rowCellPadding = parseInt(rowCell.css('font-size'));
		return parseInt($(rowCell).position().top + rowCellPadding);
	}

	function fullColumnError(colNum) {
		let col = $(document).find(`.col[data-column='${colNum}']`);
		$(col).toggleClass('col-full');
		setTimeout(function(){
			$(col).toggleClass('col-full');
		},200);
	}

	function getTokenWidth(){
		let col = $('.col')[0],
			colWidth = parseInt($(col).outerWidth()),
			tokenWidth = colWidth - (colWidth * 0.09);
		return tokenWidth;
	}

	function resetGame(){
		// TODO Also need to tell Python that the game has been reset
		removeTokens();
	}

	function removeTokens(){
		let allTokens = $('.token');
		allTokens.fadeOut('fast', function() {
			allTokens.remove();
		});					
	}

	function removePopUp(){
		let popUp = $('.pop-up'),
			overlay = $('.overlay');

		popUp.fadeOut('fast', function(){
			overlay.fadeOut();	
			popUp.removeClass().addClass('pop-up');
		});
	}

	function displayPopUp(content){
		let popUp = $('.pop-up'),
			overlay = $('.overlay');

		popUp.addClass(content[0]);
		popUp.find('p').hide();

		if (content[1]) {
			popUp.find('h1').text(content[1]);
		}			
		if (content[2]) {
			popUp.find('p').text(content[2]).show();
		}					

		overlay.fadeIn('fast', function(){
			popUp.fadeIn();	
		});
	}

	main();




// TODO	
// Reset table – tell Python the game has been reset
// Display the win line (get the col rows of all four tokens and use JS to draw the line)
	// Before you show the pop-up



// Additional - 'nice to haves'
// Highlight the four winning tokens before showing the pop-up?



// DONE 
// Speed of the token dropping
// set the position of the token when it drops (the translateY value)	
// set the token width properly
// Update the amount of bounce on the token animation
// Success messages
// Landscape alert pop-up
// Update position of tokens on resize
// Add counter to show how many wins/losses?




});